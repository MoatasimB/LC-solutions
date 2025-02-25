class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class Node:
            def __init__(self):
                self.children = {}
                self.end = False
        class Trie:
            def __init__(self):
                self.root = Node()
            
            def add(self, num):
                curr = self.root
                num = str(num)
                for digit in num:
                    if int(digit) not in curr.children:
                        curr.children[int(digit)] = Node()
                    curr = curr.children[int(digit)]
                
                curr.end = True
            
            def check(self, num):
                count = 0
                curr = self.root
                num = str(num)
                for digit in num:
                    if int(digit) in curr.children:
                        count += 1
                    else:
                        break
                    curr = curr.children[int(digit)]
                return count
        trie = Trie()

        for num in arr1:
            trie.add(num)
        
        ans = 0

        for num in arr2:
            x = trie.check(num)
            ans = max(ans, x)
        
        return ans