import unittest
from py_whisper_cipher import whisper_cipher


class TestWHhisperCipher(unittest.TestCase):
    def test_cipher_cases(self):
        self.assertEqual(whisper_cipher("hello", 3), "khoor")
        self.assertEqual(whisper_cipher("Hello World!", 1), "Ifmmp Xpsme!")
        self.assertEqual(whisper_cipher("xyz", 3), "abc")
        self.assertEqual(whisper_cipher("ABC123def", 5), "FGH123ijk")
        self.assertEqual(whisper_cipher("", 10), "")
        self.assertEqual(whisper_cipher("abc", -3), "xyz")
