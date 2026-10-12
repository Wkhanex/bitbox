import unittest

from tools.file_size_human import run


class FileSizeTests(unittest.TestCase):
    def test_nonfinite_sizes_return_errors(self):
        for text in ("nan", "NaN", "inf", "+Infinity", "-inf", "1e9999"):
            with self.subTest(text=text):
                self.assertEqual(run(text), "Error: Size must be finite.")

    def test_unit_boundaries(self):
        for text, expected in (("0", "0 B"), ("1023", "1023 B"), ("1024", "1 KB"), ("1536", "1.5 KB"), ("1048576", "1 MB")):
            with self.subTest(text=text):
                self.assertEqual(run(text), expected)

    def test_existing_validation(self):
        self.assertEqual(run("-1"), "Error: Size must be non-negative.")
        self.assertEqual(run("invalid"), "Error: Size must be a number.")
        self.assertEqual(run(), "Error: Expected exactly 1 argument.")
        self.assertEqual(run("1", "2"), "Error: Expected exactly 1 argument.")


if __name__ == "__main__":
    unittest.main()
