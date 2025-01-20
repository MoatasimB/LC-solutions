class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        commonList = [0] * 26

        for ch in words[0]:
            commonList[ord(ch) - ord('a')] +=1
        

        for i in range(1, len(words)):

            currentList = [0] * 26
            
            for ch in words[i]:
                currentList[ord(ch) - ord('a')] +=1
            
            for i in range(26):
                commonList[i] = min(commonList[i], currentList[i])
        
        ans = []
        for i in range(26):
            if commonList[i] > 0:

                ch = chr(i + ord('a'))

                for _ in range(commonList[i]):
                    ans.append(ch)
        return ans
        