import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from statistics import median

from tools.median_of_list import run


class MedianTests(unittest.TestCase):
    def test_large_integer_pair_is_exact(self):
        self.assertEqual(
            run("1000000000000000000000000000001,1000000000000000000000000000003"),
            "1000000000000000000000000000002",
        )

    def test_large_fractional_pair_is_exact(self):
        self.assertEqual(
            run("1000000000000000000000000000001.1,1000000000000000000000000000001.2"),
            "1000000000000000000000000000001.15",
        )

    def test_small_decimal_pair_is_exact(self):
        self.assertEqual(run("1e-30,2e-30"), "0.0000000000000000000000000000015")

    def test_does_not_change_callers_context(self):
        with localcontext() as context:
            context.prec = 2
            self.assertEqual(run("1234,1235"), "1234.5")
            self.assertEqual(context.prec, 2)

    def test_fraction_oracle(self):
        samples = ("3,1,2", "-99,1", "-1.5,0.25", "1,1.001", "0,1e-20", "5,2,100,3")
        for text in samples:
            values = [Fraction(Decimal(value)) for value in text.split(",")]
            with self.subTest(text=text):
                self.assertEqual(Fraction(Decimal(run(text))), median(values))

    def test_invalid_inputs_keep_errors(self):
        for text in ("", "1,", "hello"):
            self.assertEqual(run(text), "Error: Expected comma-separated numbers")
        for text in ("NaN", "1,Infinity"):
            self.assertEqual(run(text), "Error: Numbers must be finite")


if __name__ == "__main__":
    unittest.main()
