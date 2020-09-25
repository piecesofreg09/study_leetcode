class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.childrenletters = set()
        self.childrennodes = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(-1)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curnode = self.root
        for i in range(len(word)):
            if word[i] not in curnode.childrenletters:
                newNode = Node(word[i])
                curnode.childrennodes[word[i]] = newNode
                curnode.childrenletters.add(word[i])
                curnode = newNode
            else:
                curnode = curnode.childrennodes[word[i]]
        curnode.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curnode = self.root
        for i in range(len(word)):
            if word[i] not in curnode.childrenletters:
                return False
            else:
                curnode = curnode.childrennodes[word[i]]
        if curnode.end == True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curnode = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curnode.childrenletters:
                return False
            else:
                curnode = curnode.childrennodes[prefix[i]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
