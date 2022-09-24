import unittest
from services import ReadService, CleanService, MarkovModel


class TestMarkovModel(unittest.TestCase):
    def setUp(self):
        read_service = ReadService()
        read_service.text = "Alice in Wonderland"
        self.clean_service = CleanService(read_service.text)
        self.markov_model = MarkovModel(self.clean_service.clean_text, 2)

    def test_object_exists(self):
        self.assertIsNotNone(self.markov_model)

    def test_get_random_starting_sequence(self):
        self.assertEqual(
            len(self.markov_model.get_random_starting_sequence()), 2)

    def test_get_random_starting_word_type(self):
        self.assertEqual(
            type(self.markov_model.get_random_starting_sequence()), list)
