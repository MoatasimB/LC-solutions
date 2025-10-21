class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        

        def find_matches(word, phrase):
            ans = []

            curr = 0 #phrase ptr
            i = 0 #word ptr
            while i < len(word):
                j = i
                while j < len(word) and curr < len(phrase) and word[j] == phrase[curr]:
                    j += 1
                    curr += 1
                
                if curr == len(phrase):
                    ans.append(i)
                
                curr = 0
            
                i += 1
            
            return ans
        


        a_matches = find_matches(s,a)
        b_matches = find_matches(s, b)

        final = []

        for i in range(len(a_matches)):
            for j in range(len(b_matches)):
                if abs(a_matches[i] - b_matches[j]) <= k:
                    final.append(a_matches[i])
                    break
        
        return final