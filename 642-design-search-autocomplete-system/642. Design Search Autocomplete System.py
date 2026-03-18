class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.sentences = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, sentence, freq):
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = Node()
            
            curr.sentences[sentence] += freq
            curr = curr.children[ch]
        
        curr.sentences[sentence] += freq
        curr.end = True

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
      
        self.mpp = defaultdict(int) #sentence : freq
        for i in range(len(sentences)):
            self.mpp[sentences[i]] = times[i]
        self.trie = Trie()
        for i, sentence in enumerate(sentences):
            self.trie.add(sentence, self.mpp[sentence])

        self.currNode = self.trie.root
        self.currSentence = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            newSentence = "".join(self.currSentence)
            if newSentence not in self.mpp:
                freq = 1
                self.mpp[newSentence] = 1
                self.trie.add(newSentence, freq)
               
            else:
                self.mpp[newSentence] += 1
                freq = self.mpp[newSentence]
                self.trie.add(newSentence, 1)
            # print(self.seenIdx)
            # print(self.sentences)
            # print(self.mpp)
            self.currNode = self.trie.root
            self.currSentence = []
            return []
            
        
        else:
            self.currSentence.append(c)
            # print(c)
            if c in self.currNode.children:
                self.currNode = self.currNode.children[c]
                # print(self.currNode.sentences)
                ans = []
                currSentences =[ (count, sentence) for sentence, count in self.currNode.sentences.items()]
                # print("_________________________")
                # print(currSentences)
                
                currSentences.sort(key=lambda x: (-x[0], x[1]))
                # print(currSentences)
                # print("_________________________")

                return [sentence for _, sentence in currSentences[:3]]

            else:
                self.currNode = Node()
                return []

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)