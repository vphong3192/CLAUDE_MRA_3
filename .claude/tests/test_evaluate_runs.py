import copy
import unittest
from harness import load

M = load('medical-review-orchestrator/scripts/evaluate_runs.py')


class Evaluation(unittest.TestCase):
    def setUp(self):
        a = dict(case_id='easy', mode='frozen', repeat=1, variant='baseline', settings_id='fixed',
                 prompt_sha256='a'*64, corpus_sha256='b'*64,
                 usage={m: 100 for m in M.METRICS}, quality={q: 0 for q in M.QUALITY})
        a['quality']['human_reviewed'] = True
        b = copy.deepcopy(a)
        b['variant'] = 'candidate'
        b['usage']['input_tokens_total'] = 80
        self.runs = [a,b]

    def test_paired_delta_is_not_approval(self):
        r = M.compare(self.runs)
        self.assertEqual(r['status'], 'COMPARISON_READY')
        self.assertFalse(r['automatic_approval'])
        self.assertEqual(r['pairs'][0]['deltas']['input_tokens_total']['percent'], -20)

    def test_missing_usage_is_unknown(self):
        self.runs[1]['usage']['cost_usd'] = None
        r = M.compare(self.runs)
        self.assertEqual(r['status'], 'INCOMPLETE')
        self.assertIsNone(r['aggregate'])
        self.assertIsNone(r['pairs'][0]['deltas']['cost_usd'])

    def test_missing_pair(self):
        self.assertEqual(M.compare(self.runs[:1])['status'], 'INCOMPLETE')

    def test_human_scoring_required(self):
        self.runs[1]['quality']['human_reviewed'] = False
        self.assertEqual(M.compare(self.runs)['status'], 'INCOMPLETE')

    def test_critical_error_never_offset_by_savings(self):
        self.runs[1]['quality']['critical_errors'] = 1
        self.assertEqual(M.compare(self.runs)['status'], 'REGRESSION')

    def test_shared_critical_error_also_blocks(self):
        for r in self.runs: r['quality']['critical_errors'] = 1
        self.assertEqual(M.compare(self.runs)['status'], 'REGRESSION')

    def test_settings_and_corpus_must_match(self):
        for field in ('settings_id', 'corpus_sha256', 'prompt_sha256'):
            with self.subTest(field=field):
                runs=copy.deepcopy(self.runs)
                runs[1][field]='c'*64
                with self.assertRaises(ValueError): M.compare(runs)

    def test_zero_baseline_does_not_divide(self):
        self.runs[0]['usage']['repair_rounds'] = 0
        self.assertIsNone(M.compare(self.runs)['pairs'][0]['deltas']['repair_rounds']['percent'])

    def test_invalid_or_duplicate_measurements(self):
        for value in (-1, True, float('nan'), '100'):
            runs=copy.deepcopy(self.runs)
            runs[0]['usage']['cost_usd']=value
            with self.assertRaises(ValueError): M.compare(runs)
        with self.assertRaises(ValueError): M.compare(self.runs+self.runs[:1])

    def test_live_corpus_may_differ(self):
        for r in self.runs: r['mode']='live'
        self.runs[1]['corpus_sha256']='c'*64
        self.assertEqual(M.compare(self.runs)['status'], 'COMPARISON_READY')


if __name__ == '__main__':
    unittest.main()
