import unittest
from services import ReadService, CleanService, MarkovModel, GenerateService
from entities import TrieNode


class TestGenerateService(unittest.TestCase):
    def setUp(self):
        read_service = ReadService()
        read_service.text = "Alice in Wonderland"
        clean_service = CleanService(read_service.text)
        markov_model = MarkovModel(clean_service.clean_text, 2)
        starting_word = markov_model.form_the_starting_sequence([])
        self.generate_service = GenerateService(
            starting_word, markov_model.model, 2)

    def test_object_exists(self):
        self.assertIsNotNone(self.generate_service)

    def test_calculate_probability(self):
        a = TrieNode()
        b = TrieNode()
        a.frequency = 3
        b.frequency = 2
        probability = self.generate_service._GenerateService__calculate_probability(
            {"a": a, "b": b})
        self.assertEqual(probability, {"a": 0.6, "b": 0.4})

    def test_generated_text(self):
        self.assertEqual(len(self.generate_service.generated_text.split()), 10)

    def test_generated_text_type(self):
        self.assertEqual(type(self.generate_service.generated_text), str)
