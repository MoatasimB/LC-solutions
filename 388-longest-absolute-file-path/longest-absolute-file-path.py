class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        lines = input.split('\n')
        depth = {0:0}

        def count_tabs_and_word(word):
            d = 0
            i = 0
            while word[i] == '\t':
                d += 1
                i += 1
            
            return [d, word[i:]]
        ans = 0
        for line in lines:
            d, word = count_tabs_and_word(line)

            if '.' in word:
                ans = max(ans, depth[d] + len(word))
            else:
                depth[d + 1] = depth[d] + len(word) + 1
        
        return ans

        
