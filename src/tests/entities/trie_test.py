import unittest
from entities import Trie


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_trie_exists(self):
        self.assertTrue(self.trie)

    def test_trie_has_root(self):
        self.assertTrue(self.trie.root)

    def test_insert(self):
        self.trie.insert(("a", "b", "c"))
        self.assertTrue(
            self.trie.root.children["a"].children["b"].children["c"].is_sequence)

    def test_get_children(self):
        self.trie.insert(("a", "b", "c"))
        self.assertTrue(self.trie.get_children(("a", "b"))["c"].is_sequence)

    def test_get_invalid_children(self):
        self.trie.insert(("a", "b", "c"))
        self.assertEqual(self.trie.get_children(("a", "d")), None)
