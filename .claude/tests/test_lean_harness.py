"""Adversarial checks of lean linkage and context selection; no LLM or network."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from harness import load, REPO

LINK = load('citation-verification/scripts/verify_claim_links.py')
SELECT = load('medical-review-orchestrator/scripts/select_lessons.py')
RENDER = load('medical-review-orchestrator/scripts/render_artifacts.py')


class ClaimLinks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.quote = 'The primary outcome occurred in 42.9% of participants after treatment during follow-up.'
        (self.root / 'paper.txt').write_text('PMID:33652425\n' + self.quote, encoding='utf-8')
        self.cards = [dict(card_id='REF-001-c1', study_id='pmid:33652425', claim='Outcome 42.9%.',
                           quote=self.quote, source_file='paper.txt', tier='abstract')]
        self.text = 'Outcome occurred in 42.9% [1].'
        self.draft = self.text + ' <!-- claim:CLM-001 -->\n\n## References\n1. Trial. PMID:33652425.\n'
        self.links = [dict(claim_id='CLM-001', text=self.text, card_ids=['REF-001-c1'],
                           citation_numbers=[1], study_ids=['pmid:33652425'])]

    def result(self):
        return LINK.validate(self.draft, self.cards, self.links, self.root)

    def fails(self, code):
        r = self.result()
        self.assertEqual(r['status'], 'FAIL')
        self.assertIn(code, {e['code'] for e in r['errors']})

    def test_valid(self):
        self.assertEqual(self.result()['status'], 'PASS')

    def test_whitespace_and_next_line_annotation(self):
        self.draft = self.draft.replace(' <!--', '\n<!--').replace('Outcome occurred', 'Outcome\n occurred')
        self.assertEqual(self.result()['status'], 'PASS')

    def test_stale_text(self):
        self.draft = self.draft.replace('occurred', 'was observed')
        self.fails('STALE_TEXT')

    def test_writer_changed_number_and_updated_mapping(self):
        self.draft = self.draft.replace('42.9', '94.2')
        self.links[0]['text'] = self.text.replace('42.9', '94.2')
        self.fails('DRAFT_NUMBER')

    def test_missing_annotation(self):
        self.draft = self.draft.replace(' <!-- claim:CLM-001 -->', '')
        self.fails('MISSING_ANNOTATION')

    def test_missing_mapping(self):
        self.links = []
        self.fails('MISSING_LINK')

    def test_orphan_mapping(self):
        self.links[0]['claim_id'] = 'CLM-other'
        self.fails('ORPHAN_LINK')

    def test_duplicate_mapping(self):
        self.links.append(copy.deepcopy(self.links[0]))
        self.fails('LINK_SCHEMA')

    def test_dangling_card(self):
        self.links[0]['card_ids'] = ['missing']
        self.fails('DANGLING_CARD')

    def test_wrong_reference(self):
        self.draft = self.draft.replace('PMID:33652425', 'PMID:37634145')
        self.fails('CITATION_IDENTITY')

    def test_wrong_study_mapping(self):
        self.links[0]['study_ids'] = ['pmid:37634145']
        self.fails('STUDY_SET')

    def test_rejected_quote(self):
        self.cards[0]['quote'] = 'This invented passage contains 42.9% but is absent from the paper.'
        self.fails('CARD_QUOTE')

    def test_empty_card_array(self):
        self.links[0]['card_ids'] = []
        self.fails('LINK_SCHEMA')

    def test_boolean_is_not_reference_number(self):
        self.links[0]['citation_numbers'] = [True]
        self.fails('LINK_SCHEMA')

    def test_fulltext_needs_abstract(self):
        self.cards[0]['tier'] = 'fulltext'
        self.fails('CARD_SCHEMA')

    def test_fulltext_rejects_abstract_quote(self):
        self.cards[0].update(tier='fulltext', abstract=self.quote)
        self.fails('CARD_FULLTEXT')

    def test_source_traversal(self):
        self.cards[0]['source_file'] = '../paper.txt'
        self.fails('CARD_SCHEMA')

    def test_table_row(self):
        row = '| Outcome | 42.9% [1] |'
        self.draft = '| Outcome | Value |\n|---|---|\n' + row + '\n<!-- claim:CLM-001 -->\n\n## References\n1. Trial. PMID:33652425.'
        self.links[0]['text'] = row
        self.assertEqual(self.result()['status'], 'PASS')

    def test_uncited_claim_is_explicit_residual(self):
        self.draft = 'An uncited qualitative claim.\n\n' + self.draft
        r = self.result()
        self.assertEqual(r['status'], 'PASS')
        self.assertIn('Uncited claims', r['limits'])

    def test_cli_real_files_and_malformed_input(self):
        for name, value in [('cards', self.cards), ('links', self.links)]:
            (self.root / name).write_text('\n'.join(json.dumps(x) for x in value), encoding='utf-8')
        (self.root / 'draft').write_text(self.draft, encoding='utf-8')
        cmd = [sys.executable, '-X', 'utf8', LINK.__file__, '--draft', str(self.root/'draft'),
               '--cards', str(self.root/'cards'), '--links', str(self.root/'links'),
               '--source-dir', str(self.root), '--out', str(self.root/'report')]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertEqual(json.loads((self.root/'report').read_text())['inputs']['draft'], RENDER.digest(self.root/'draft'))
        (self.root/'links').write_text('{broken', encoding='utf-8')
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(r.returncode, 1)


class LessonSelection(unittest.TestCase):
    def test_role_and_scope_intersection(self):
        text = '''### L-001: Writer universal
- **Role:** writer
- **Scope:** universal
### L-002: Appraiser domain
- **Role:** appraiser
- **Scope:** cardiology-ep
### L-003: Writer language
- **Role:** synthesis-writer
- **Scope:** vi-language
### L-004: Unknown scope
- **Role:** writer
- **Scope:** future-scope
'''
        lead = SELECT.select(text, ['lead'], ['universal'])
        self.assertIn('L-001', lead)
        self.assertIn('L-004', lead)
        self.assertNotIn('L-002', lead)
        self.assertNotIn('L-003', lead)
        self.assertIn('L-003', SELECT.select(text, ['lead'], ['vi-language']))
        self.assertNotIn('L-002', SELECT.select(text, ['appraiser'], []))
        self.assertIn('L-002', SELECT.select(text, ['appraiser'], ['cardiology-ep']))

    def test_missing_scope_included(self):
        self.assertIn('L-001', SELECT.select('### L-001: Rule\n- **Role:** verifier\n', ['verifier'], []))

    def test_all_roles_included(self):
        self.assertIn('L-001', SELECT.select('### L-001: Rule\n- **Role:** all\n', ['retriever'], []))


class LeanWiring(unittest.TestCase):
    def test_default_roles_and_removed_workers(self):
        agents = {p.stem for p in (REPO/'.claude/agents').glob('*.md')}
        self.assertEqual(agents, {'review-lead', 'evidence-retriever', 'critical-appraiser', 'citation-verifier', 'quality-coach'})

    def test_render_missing_certainty_refused(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/'cards.jsonl'
            path.write_text('{"card_id":"one"}', encoding='utf-8')
            with self.assertRaises(ValueError):
                RENDER.read_cards(path)

    def test_evidence_cells_escape_pipes(self):
        cards = [dict(card_id='one', study_id='pmid:33652425', outcome='A|B', claim='42.9%', certainty='Low')]
        result = RENDER.evidence(cards)
        self.assertIn('A\\|B', result)
        self.assertIn('not recorded', result)


if __name__ == '__main__':
    unittest.main()
