import unittest
from src.codebook_parser import parse_codebook


class TestCodebookParser(unittest.TestCase):
    """Test for parse_codebook function.
    
    These tests together verify that the parser correctly extracts the codebook values
    We test 3 representative cases
    - AA4 as a standard categorical variable (Yes, No, DK, NA pattern)
    - BA50 as the master branching variable with exactly 3 codes
    - AG2 as a continuous variable which should not have code mapping
    """

    @classmethod
    def setUpClass(cls):
        """Parse the codebook once for all tests
        Parsing is slow so we want to re-use the parsed values for each method tested
        """
        cls.codebook = parse_codebook("data/37202-0003-Codebook-waves_MULTI.pdf")

    def test_aa4_has_correct_codes(self):
        """AA4 should decode to Yes, No, DK, NA (from codebook pg. 6)"""
        aa4 = self.codebook['AA4']
        self.assertEqual(aa4['codes'][1], 'Yes')
        self.assertEqual(aa4['codes'][5], 'No')
        self.assertEqual(aa4['codes'][8], 'DK')
        self.assertEqual(aa4['codes'][9], 'NA')

    def test_ba50_has_three_broaching_codes(self):
        """BA50 is the master branching variable with 3 values (from codebook p.59)"""
        ba50 = self.codebook['BA50']
        self.assertIn(1, ba50['codes'])
        self.assertIn(2, ba50['codes'])
        self.assertIn(3, ba50['codes'])
        self.assertEqual(len(ba50['codes']), 3)

    def test_ag2_is_continuous(self):
        """AG2 owner count should be continuous"""
        ag2 = self.codebook['AG2']
        self.assertEqual(ag2['type'], 'continuous')

if __name__ == "__main__":
    unittest.main()
