class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete_word = False
        self.words_counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, value):
        node = self.root
        for i in value:
            char_code = ord(i) - ord('a')
            if char_code not in node.children.keys():
                node.children[char_code] = TrieNode()
            node = node.children[char_code]
            node.words_counter = node.words_counter + 1
        node.is_complete_word = True

    def is_word_exist(self, value):
        node = self.root
        result = None
        for i in value:
            char_code = ord(i) - ord('a')
            if char_code in node.children.keys():
                result = node.children[char_code]
                node = node.children[char_code]
            else:
                return False
        if result == -1:
            return False
        else:
            return result.is_complete_word


if __name__ == "__main__":
    trie_based_on_children = Trie()
    trie_based_on_children.add("abcdefghij")
    trie_based_on_children.add("abcdefghijklm")
    assert trie_based_on_children.is_word_exist("abcde") is False
    assert trie_based_on_children.is_word_exist("abcdee") is False
    assert trie_based_on_children.is_word_exist("abcdefghi") is False
    assert trie_based_on_children.is_word_exist("abcdefghij") is True
    assert trie_based_on_children.is_word_exist("abcdefghijklm") is True

    trie_based_on_children2 = Trie()
    trie_based_on_children.add("very_long_words")
    trie_based_on_children.add("very_long")
    assert trie_based_on_children.is_word_exist("very_long_words")
    assert trie_based_on_children.is_word_exist("very_long")
    assert trie_based_on_children.is_word_exist("very_") is False
    assert trie_based_on_children.is_word_exist("very_long_word") is False
