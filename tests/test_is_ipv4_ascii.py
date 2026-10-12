import ipaddress
import unittest

from tools.is_ipv4 import run


class IPv4Tests(unittest.TestCase):
    def test_ascii_addresses(self):
        for text in ("0.0.0.0", "127.0.0.1", "255.255.255.255", "192.168.1.1"):
            with self.subTest(text=text):
                self.assertEqual(run(text), "True")

    def test_invalid_addresses(self):
        for text in ("", "1.2.3", "1.2.3.4.5", "256.1.1.1", "01.2.3.4", "-1.2.3.4", "1.2.3. 4"):
            with self.subTest(text=text):
                self.assertEqual(run(text), "False")

    def test_unicode_digits_are_rejected(self):
        for text in ("١٢٧.0.0.١", "１２７.0.0.1", "².1.1.1", "1.1.1.₂"):
            with self.subTest(text=text):
                self.assertEqual(run(text), "False")

    def test_matches_stdlib_at_octet_boundaries(self):
        for octet in (-1, 0, 1, 9, 10, 127, 254, 255, 256):
            for position in range(4):
                parts = ["1"] * 4
                parts[position] = str(octet)
                text = ".".join(parts)
                try:
                    ipaddress.IPv4Address(text)
                    expected = "True"
                except ipaddress.AddressValueError:
                    expected = "False"
                with self.subTest(text=text):
                    self.assertEqual(run(text), expected)


if __name__ == "__main__":
    unittest.main()
