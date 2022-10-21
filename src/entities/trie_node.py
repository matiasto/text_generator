class TrieNode:
    """ Represents a node in the Trie datastructure. """

    def __init__(self):
        self.children = {}
        self.is_sequence = False
        self.frequency = 0
