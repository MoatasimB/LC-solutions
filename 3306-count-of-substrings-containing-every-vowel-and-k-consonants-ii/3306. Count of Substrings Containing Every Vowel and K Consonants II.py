class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def sw(k):
            vowels = defaultdict(int)
            constants = 0

            l = 0
            ans = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowels[word[r]] +=1
                else:
                    constants += 1
                
                while len(vowels) == 5 and constants >= k:
                    ans += len(word) - r

                    if word[l] in "aeiou":
                        vowels[word[l]] -=1
                        if vowels[word[l]] == 0:
                            del vowels[word[l]]
                    else:
                        constants -= 1
                    l += 1
            
            return ans

        return sw(k) - sw(k+1)
