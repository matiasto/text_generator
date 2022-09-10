import unittest
from services import TextService


class TestTextService(unittest.TestCase):
    def setUp(self):
        self.text_service = TextService("test")

    def test_index_text(self):
        self.assertEqual(self.text_service.text, "test")
