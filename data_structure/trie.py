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
        for i in value:
            char_code = ord(i) - ord('a')
            if char_code in node.children.keys():
                node = node.children[char_code]
            else:
                return False
        return node.is_complete_word

    def remove(self, value):
        node = self.root
        for i in value:
            char_code = ord(i) - ord('a')
            if char_code in node.children.keys():
                node = node.children[char_code]
                node.words_counter = node.words_counter - 1
            else:
                return False
        node.is_complete_word = False
        return True


if __name__ == "__main__":
    trie_ds = Trie()
    trie_ds.add("abcdefghij")
    trie_ds.add("abcdefghijklm")
    assert trie_ds.is_word_exist("abcde") is False
    assert trie_ds.is_word_exist("abcdee") is False
    assert trie_ds.is_word_exist("abcdefghi") is False
    assert trie_ds.is_word_exist("abcdefghij") is True
    assert trie_ds.is_word_exist("abcdefghijklm") is True

    trie_ds2 = Trie()
    trie_ds2.add("longword")
    trie_ds2.add("word")
    assert trie_ds2.is_word_exist("longword")
    assert trie_ds2.is_word_exist("word")
    assert trie_ds2.is_word_exist("longw") is False
    assert trie_ds2.is_word_exist("longwords") is False
    if trie_ds2.is_word_exist("word"):
        assert trie_ds2.remove("word")
    assert trie_ds2.is_word_exist("word") is False
    assert trie_ds2.is_word_exist("longword")
    assert trie_ds2.is_word_exist("zxc") is False