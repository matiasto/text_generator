from .trie_node import TrieNode


class Trie:
    """ Represents a trie data structure.

    The trie is used to store sequences of words and their frequencies.

    Attributes:
        root (TrieNode): The root node of the trie.
    """

    def __init__(self) -> None:
        """Initializes the trie"""

        self.__root = TrieNode()

    def insert(self, sequence) -> None:
        """Inserts a sequence into the trie.

        Args:
            sequence (list): The word sequence to be inserted.
        """

        node = self.__root
        for word in sequence:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_sequence = True
        node.frequency += 1

    def get_children(self, sequence: list) -> dict:
        """Returns the children of a sequence.

        Args:
            sequence (list): The sequence to get the children of.

        Returns:
            dict: The children of the sequence.
        """

        node = self.__root
        if not sequence:
            return node.children
        for word in sequence:
            if word not in node.children:
                return None
            node = node.children[word]
        return node.children
