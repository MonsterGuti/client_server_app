import unittest
from auth import (
    is_valid_name, is_valid_email, is_valid_password,
    hash_password, verify_password, create_captcha
)

class TestAuth(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("martingogulanov@gmail.com"))
        self.assertFalse(is_valid_email("invalid-email"))

    def test_valid_name(self):
        self.assertTrue(is_valid_name("Martin"))
        self.assertFalse(is_valid_name("M3rtin"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("StrongPass1"))
        self.assertFalse(is_valid_password("short"))
        self.assertFalse(is_valid_password("withoutupper3"))
        self.assertFalse(is_valid_password("WITHOUTLOWER"))

    def test_hash_and_verify_password(self):
        password = "Marti2005"
        hashed = hash_password(password)
        self.assertTrue(verify_password(password, hashed))
        self.assertFalse(verify_password("other", hashed))

    def test_generate_captcha(self):
        captcha_code = create_captcha()
        self.assertEqual(len(captcha_code), 6)
        self.assertTrue(captcha_code.isalnum())

if __name__ == '__main__':
    unittest.main()
