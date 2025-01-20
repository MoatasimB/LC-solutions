class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        

        def check(word1, word2):


            for x in range(len(word1)):
                i = x
                j = 0
                while i<len(word1) and j <len(word2):

                    if word1[i] != word2[j]:
                        break
                    i+=1
                    j+=1
                
                if j == len(word2):
                    return True
            return False
        
        ans = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if check(words[j], words[i]):
                        ans.append(words[i])
                        break
        return ans