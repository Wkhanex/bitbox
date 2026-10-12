import unittest
from tools.word_lengths import run


class ToolTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('2,5', run(*('hi there',)))

    def test_case_2(self):
        self.assertEqual('', run(*('',)))

    def test_case_3(self):
        self.assertEqual('', run(*(' \t\n ',)))

    def test_case_4(self):
        self.assertEqual('3,3,5', run(*('one\ttwo\nthree',)))

    def test_case_5(self):
        self.assertEqual('4,1', run(*('élan 🌍',)))

    def test_invalid_arguments(self):
        for args in [(), ('a', 'b')]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
