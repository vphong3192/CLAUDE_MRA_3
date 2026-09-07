"""Manifest must reject stale inputs and unresolved decisions rather than certify current bytes."""
import json
import tempfile
import unittest
from pathlib import Path
from harness import load

M = load('medical-review-orchestrator/scripts/render_artifacts.py')


class Manifest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ws = self.root/'_workspace'
        self.ws.mkdir()
        self.src = self.root/'source'
        self.src.mkdir()
        (self.src/'paper.txt').write_text('synthetic source fixture', encoding='utf-8')
        self.store = self.root/'store.md'
        self.store.write_text('synthetic store fixture', encoding='utf-8')
        for name in ['00_scope.md','01_protocol.md','02_corpus.md','02a_search_log.md','02j_prisma.md',
                     '03_research_map.md','03a_gate_approval.md','04_appraisal.md','04c_quote_locks.md',
                     '04d_evidence_table.md','05b_claim_links.jsonl','06_final_review.md',
                     '06a_verification_report.md','06b_citation_audit.md']:
            (self.ws/name).write_text('synthetic '+name, encoding='utf-8')
        self.cards=[dict(card_id='C1',study_id='pmid:33652425',claim='Synthetic claim',
                         certainty='Low',outcome='synthetic outcome',source_file='paper.txt')]
        (self.ws/'04b_cards.jsonl').write_text(json.dumps(self.cards[0]),encoding='utf-8')
        self.state=dict(run_id='synthetic-test',scope=dict(status='approved',receipt='TEST fixture'),
                        research_map=dict(status='approved',receipt='TEST fixture',sha256=M.digest(self.ws/'03_research_map.md')),
                        appraisal_decision=dict(status='not_needed',reason='TEST'),coach=dict(status='not_needed',reason='TEST'),
                        qa=dict(status='PASS',draft_sha256=M.digest(self.ws/'06_final_review.md')),learning=dict(status='no_new_lesson'))
        self.audit=dict(status='PASS',inputs=dict(draft=M.digest(self.ws/'06_final_review.md'),
                         cards=M.digest(self.ws/'04b_cards.jsonl'),links=M.digest(self.ws/'05b_claim_links.jsonl'),
                         sources={'paper.txt':M.digest(self.src/'paper.txt')}))
        self.save()

    def save(self):
        (self.ws/'00a_run.json').write_text(json.dumps(self.state),encoding='utf-8')
        (self.ws/'06d_claim_audit.json').write_text(json.dumps(self.audit),encoding='utf-8')

    def render(self):
        self.save()
        return M.manifest(self.ws,self.store,self.src,self.ws/'06c_manifest.md')

    def test_valid_index_is_deterministic_not_certification(self):
        result=self.render()
        self.assertEqual(result,self.render())
        self.assertIn('not a new semantic review',result)
        self.assertIn(M.digest(self.src/'paper.txt'),result)

    def test_map_changed_after_approval(self):
        (self.ws/'03_research_map.md').write_text('changed')
        with self.assertRaisesRegex(ValueError,'Map changed'): self.render()

    def test_draft_changed_after_qa(self):
        (self.ws/'06_final_review.md').write_text('changed')
        with self.assertRaisesRegex(ValueError,'draft changed'): self.render()

    def test_source_changed_after_claim_check(self):
        (self.src/'paper.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError,'Claim audit stale'): self.render()

    def test_cards_changed_after_claim_check(self):
        self.cards[0]['claim']='different'
        (self.ws/'04b_cards.jsonl').write_text(json.dumps(self.cards[0]))
        with self.assertRaisesRegex(ValueError,'Claim audit stale'): self.render()

    def test_pending_or_missing_approval(self):
        self.state['research_map']['status']='pending'
        with self.assertRaisesRegex(ValueError,'not approved'): self.render()

    def test_pending_appraisal_blocks(self):
        self.state['appraisal_decision']['status']='pending'
        with self.assertRaisesRegex(ValueError,'Appraisal decision'): self.render()

    def test_approved_appraisal_needs_reply(self):
        self.state['appraisal_decision']['status']='approved'
        with self.assertRaisesRegex(ValueError,'needs receipt'): self.render()

    def test_coach_receipt_missing(self):
        self.state['coach']['status']='completed'
        with self.assertRaisesRegex(ValueError,'report missing'): self.render()

    def test_failed_or_unbound_claim_report(self):
        self.audit['status']='FAIL'
        with self.assertRaisesRegex(ValueError,'Claim audit failed'): self.render()
        self.audit={'status':'PASS'}
        with self.assertRaisesRegex(ValueError,'Claim audit stale'): self.render()


if __name__=='__main__':
    unittest.main()
