class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        def val(c):
            return ord(c) - ord('a') + 1
        def find_matches(word, phrase):
            ans = []
            if len(phrase) > len(word):
                return ans 
            MOD = 10**9 + 7
            highest_power = 1
            k = 31
            for _ in range(len(phrase) - 1):
                highest_power *= k
            
            phrase_hash = 0
            for i in range(len(phrase)):
                ch = phrase[i]
                phrase_hash = (phrase_hash * k + val(ch))% MOD
       
            curr = 0
            for i in range(len(phrase)):
                ch = word[i]
                curr = (curr * k + val(ch)) % MOD

            if phrase_hash == curr:
                ans.append(0)
            
            for i in range(len(phrase), len(word)):
                old_ch = word[i - len(phrase)]
                curr -= (val(old_ch) * highest_power)
                

                ch = word[i]
                curr = (curr * k + val(ch)) % MOD


                if curr == phrase_hash and word[i-len(phrase) + 1: i+1] == phrase:
                    ans.append(i - len(phrase) + 1)



            return ans
        

        a_matches = find_matches(s,a)
        b_matches = find_matches(s,b)

        print(a_matches)
        print(b_matches)
        final = []

        for i in range(len(a_matches)):
            for j in range(len(b_matches)):
                if abs(a_matches[i] - b_matches[j]) <= k:
                    final.append(a_matches[i])
                    break
        
        return final