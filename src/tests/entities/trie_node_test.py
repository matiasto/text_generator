import unittest
from entities import TrieNode


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.trie_node = TrieNode()
        self.trie_node.children = {"a": TrieNode(), "b": TrieNode()}
        self.trie_node.frequency = 1

    def test_node_exists(self):
        self.assertTrue(self.trie_node)

    def test_node_has_children(self):
        self.assertTrue(self.trie_node.children)

    def test_node_has_frequency(self):
        self.assertTrue(self.trie_node.frequency)
