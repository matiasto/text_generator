import unittest
from services import ReadService, CleanService


class TestCleanService(unittest.TestCase):
    def setUp(self):
        read_service = ReadService()
        read_service.text = "Alice in Wonderland"
        self.clean_service = CleanService(read_service.text)

    def test_object_exists(self):
        self.assertIsNotNone(self.clean_service)

    def test_clean_text_has_data(self):
        self.assertGreater(len(self.clean_service.clean_text), 0)

    def test_clean_text_type(self):
        self.assertEqual(type(self.clean_service.clean_text), list)
