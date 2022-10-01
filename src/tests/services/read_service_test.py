import unittest
from services import ReadService


class TestReadService(unittest.TestCase):
    def setUp(self):
        self.text_service = ReadService()

    def test_object_exists(self):
        self.assertIsNotNone(self.text_service)

    def test_title(self):
        self.text_service.text = "Alice in Wonderland"
        self.assertEqual(self.text_service.title, "Alice in Wonderland")

    def test_available_stories(self):
        self.assertEqual(len(self.text_service.available_stories), 4)

    def test_text(self):
        self.text_service.text = "Alice in Wonderland"
        self.assertEqual(len(self.text_service.text), 3759)

    def test_text_invalid(self):
        with self.assertRaises(Exception) as context:
            self.text_service.text = "Invalid"

    def test_text_invalid_type(self):
        with self.assertRaises(Exception) as context:
            self.text_service.text = 1
