"""Tests for the Counter exercises. Run with: python3 -m unittest -v"""

import unittest

from exercises import are_anagrams, can_construct, frequency_map, top_k_frequent


class CounterExercisesTest(unittest.TestCase):
    def test_frequency_map(self) -> None:
        self.assertEqual(frequency_map([4, 4, 2, 4, 2]), {4: 3, 2: 2})
        self.assertEqual(frequency_map([]), {})

    def test_anagrams(self) -> None:
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertFalse(are_anagrams("rat", "car"))
        self.assertFalse(are_anagrams("aab", "abb"))

    def test_can_construct(self) -> None:
        self.assertTrue(can_construct("apple", "palepeople"))
        self.assertFalse(can_construct("apple", "alepeople"))
        self.assertTrue(can_construct("", "anything"))

    def test_top_k_frequent(self) -> None:
        self.assertEqual(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent([4, 4, 1, 1, 3], 2), [1, 4])
        self.assertEqual(top_k_frequent([-1, -1, 2], 1), [-1])


if __name__ == "__main__":
    unittest.main()
