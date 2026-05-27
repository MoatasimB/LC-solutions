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
                str_num = str(num)
                curr = self.root

                for digit in str_num:
                    if int(digit) not in curr.children:
                        curr.children[int(digit)] = Node()
                    curr = curr.children[int(digit)]
                
                curr.end = True
            
            def check(self, num):
                str_num = str(num)
                curr = self.root
                ans = 0
                
                for digit in str_num:
                    if int(digit) in curr.children:
                        ans += 1
                    else:
                        break
                    curr = curr.children[int(digit)]
                return ans
        
        T = Trie()

        for num in arr1:
            T.add(num)
        
        ans = 0

        for num in arr2:
            ans = max(ans, T.check(num))
        
        return ans
                        