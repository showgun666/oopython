"Module for Trie Class"
from src.node import Node
from src.exceptions import SearchMiss

class Trie:
    "Class for trie object"

    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        "adds word to Trie"
        node = self.root
        word = word.lower().strip()
        # Iterate over letters in word
        for character in word:
            if character not in node.children:
                node.children[character] = Node()
            node = node.children[character]

        # At last letter, set is_end_of_word to True
        node.is_end_of_word = True

    def find_word(self, word):
        "check if word exists in Trie, returns boolean"
        word = word.lower().strip()
        node = self.root

        for character in word:
            if character not in node.children:
                return False # ADD ERROR
            node = node.children[character]
        return node.is_end_of_word

    def remove_word(self, word):
        "method to remove words from trie"
        word = word.lower().strip()
        def _remove(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    raise SearchMiss(f'Word "{word}" not found in trie')
                node.is_end_of_word = False
                return len(node.children) == 0
            character = word[depth]
            if character not in node.children:
                raise SearchMiss(f'Word "{word}" not found in trie')
            should_delete_child = _remove(node.children[character], word, depth + 1)
            if should_delete_child:
                del node.children[character]
                return len(node.children) == 0
            return False
        _remove(self.root, word, 0)

    def count_words(self):
        "returns words in Trie as integer"
        def _count_words(node):
            count = 1 if node.is_end_of_word else 0
            for child in node.children.values():
                count += _count_words(child)
            return count
        return _count_words(self.root)

    def get_words(self):
        "returns all words in Trie"
        words = []

        def _get_words(node, prefix):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _get_words(child, prefix + char)

        _get_words(self.root, "")
        return sorted(words)

    def prefix_search(self, prefix):
        "returns all words prefixed with prefix as list by iterating over Trie"
        node = self.root
        prefix = prefix.lower().strip()
        for character in prefix:
            if character not in node.children:
                return []
            node = node.children[character]

        words = []

        def _get_words(node, current_prefix):
            if node.is_end_of_word:
                words.append(current_prefix)
            for character, child in node.children.items():
                _get_words(child, current_prefix + character)
        _get_words(node, prefix)
        return sorted(words)

    @classmethod
    def create_from_file(cls, file):
        "returns Trie object with entries from file"
        instance = cls()
        with open(file, "r", encoding="utf-8") as file:
            for line in file:
                instance.add_word(line.strip())
        return instance
