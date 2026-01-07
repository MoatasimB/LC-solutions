class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # b a l l 
        # a r e a
        # l e a d
        # l a d y


        #prefix : [] words

        prefixToWord = defaultdict(list)

        for word in words:
            for j in range(len(word)):
                prefixToWord[word[:j + 1]].append(word)
        
        ans = []
        def dfs(step, curr):
            if step == len(words[0]):
                ans.append(curr[:])
                return
            
            if not curr:
                for word in words:
                    curr.append(word)
                    dfs(1, curr)
                    curr.pop()
            else:
                prefix = "".join([word[step] for word in curr])
                # prevWord = curr[-1]
                # prefix = prevWord[:len(curr)]
                # print(curr, prefix)

                for word in prefixToWord[prefix]:
                    curr.append(word)
                    dfs(step + 1, curr)
                    curr.pop()
        
        dfs(0, [])
        return ans

        # a r e a
        # r 
        # e
        # a