class Node:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int) #sentence/freq

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addSentence(self, sentence, count):
        curr = self.root

        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.sentences[sentence] += count
        

class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.addSentence(sentences[i], times[i])
        
        self.currNode = self.trie.root
        self.currSentence = []

    def input(self, c: str) -> list[str]:
        # print(c, self.currSentence)
        if c == "#":
            sentence = "".join(self.currSentence)
            self.currSentence = []
            self.currNode = self.trie.root
            self.trie.addSentence(sentence, 1)
            return []
        else:
            self.currSentence.append(c)
            if c not in self.currNode.children:
                self.currNode.children[c] = Node()
                self.currNode = self.currNode.children[c]
                return []
            else:
                self.currNode = self.currNode.children[c]
                #get top 3
                ans = []
                sortedSentences = sorted(self.currNode.sentences.items(), key = lambda x: (-x[1], x[0]))
                # print(sortedSentences[:3])
                for i in range(min(3, len(sortedSentences))):
                    ans.append(sortedSentences[i][0])
                return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)