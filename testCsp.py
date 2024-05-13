import unittest

import CSP


class TestAddNumbers(unittest.TestCase):

    def test_valid_row(self):
        result = CSP.valid_row('0101', [1, 1])
        self.assertTrue(result)
        result1 = CSP.valid_row('011101', [3, 1])
        self.assertTrue(result1)

    def test_get_positions(self):
        result = CSP.getPosition('0101', [1, 1])
        self.assertEqual(result, [[1, 1], [3, 3]])
        result1 = CSP.getPosition('011101', [3, 1])
        self.assertEqual(result1, [[1, 3], [5, 5]])

    def test_getActions(self):
        result = CSP.getActions('0101', [1, 1])
        self.assertEqual(result, ['L', 'R'])


if __name__ == '__main__':
    unittest.main()
