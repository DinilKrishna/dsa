class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def remove(self, word):
        self._remove(self.root, word, 0)

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _remove(self, node, word, depth):
        if not node:
            return None

        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                return len(node.children) == 0
            return False

        char = word[depth]
        if char not in node.children:
            return False

        should_delete_current_node = self._remove(node.children[char], word, depth + 1)

        if should_delete_current_node:
            del node.children[char]
            return len(node.children) == 0

        return False
    
    def search_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # Prefix not found, return an empty list
            current = current.children[char]

        words = []
        self._collect_words(current, prefix, words)
        return words

    def _collect_words(self, node, current_word, words):
        if node.is_end_of_word:
            words.append(current_word)

        for char, child in node.children.items():
            self._collect_words(child, current_word + char, words)
    
    def suf_insert(self, word):
        if word is None or len(word) == 0:
            return
        current = self.root
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                current.children[w] = TrieNode()
        current.end_of_word = True
        self.suf_insert(word[1:])

# Example Usage:
trie = Trie()
words = ["apple", "app", "application", "banana", "bat"]
for word in words:
    trie.insert(word)

print("Search 'app':", trie.search("appl"))  # Output: True
print("Search 'apples':", trie.search("apples"))  # Output: False

print("Starts with 'ban':", trie.starts_with("ban"))  # Output: True
print("Starts with 'batman':", trie.starts_with("batman"))  # Output: False

print("Before removal - Search 'apple':", trie.search("apple"))  # Output: True
trie.remove("apple")
print("After removal - Search 'apple':", trie.search("apple"))  # Output: False