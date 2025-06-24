class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        s_ptr = 0
        a_ptr = 0

        while a_ptr < len(abbr):
            if s_ptr >= len(word):
                return False

            if abbr[a_ptr].isalpha():
                if word[s_ptr] != abbr[a_ptr]:
                    return False
                
                s_ptr += 1
                a_ptr += 1
                continue
            
            else:
                skip = 0
                while a_ptr < len(abbr) and not abbr[a_ptr].isalpha():
                    skip = (skip * 10) + int(abbr[a_ptr])
                    if skip == 0:
                        return False
                    a_ptr += 1
                
                s_ptr += skip
        
        return s_ptr == len(word)
            
                

            
