class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root =  TrieNode()
    
    def insert(self, word):
        current = self.root
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                current.children[w] = TrieNode()
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        if current.end_of_word == True:
            return True
        return False
    
    def start_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        return True

    def remove_word(self, word):
        current = self.root
        