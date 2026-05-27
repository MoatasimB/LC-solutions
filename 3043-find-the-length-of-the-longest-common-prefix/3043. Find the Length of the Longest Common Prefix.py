class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True
    
    def find(self, word):
        count = 0
        curr = self.root
        for ch in word:
            if ch in curr.children:
                count += 1
                curr = curr.children[ch]
            else:
                break
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        n1 = len(arr1)
        n2 = len(arr2)

        t = Trie()

        for num in arr1:
            str_num = str(num)
            t.add(str_num)
        ans = 0
        for num in arr2:
            str_num = str(num)
            length = t.find(str_num)
            ans = max(ans, length)
        
        return ans

