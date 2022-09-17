import unittest
from services import ReadService, CleanService, MarkovModel, GenerateService


class TestGenerateService(unittest.TestCase):
    def setUp(self):
        read_service = ReadService()
        read_service.text = "Alice in Wonderland"
        clean_service = CleanService(read_service.text)
        markov_model = MarkovModel(clean_service.clean_text)
        starting_word = markov_model.get_random_starting_word()
        self.generate_service = GenerateService(
            starting_word, markov_model.model)

    def test_object_exists(self):
        self.assertIsNotNone(self.generate_service)

    def test_generated_text(self):
        self.assertEqual(len(self.generate_service.generated_text.split()), 22)

    def test_generated_text_type(self):
        self.assertEqual(type(self.generate_service.generated_text), str)
