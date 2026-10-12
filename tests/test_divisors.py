import unittest
from tools.divisors import run


class DivisorTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual("1,2,3,4,6,12", run("12"))

    def test_one(self):
        self.assertEqual("1", run("1"))

    def test_prime(self):
        self.assertEqual("1,97", run("97"))

    def test_perfect_square_has_no_duplicate_root(self):
        self.assertEqual("1,2,3,4,6,9,12,18,36", run("36"))

    def test_matches_naive_divisors_for_small_positive_integers(self):
        for n in range(1, 200):
            expected = ",".join(str(i) for i in range(1, n + 1) if n % i == 0)
            self.assertEqual(expected, run(str(n)))

    def test_invalid_input(self):
        for args in (("0",), ("-12",), ("3.5",), ("hello",), (), ("12", "extra")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
