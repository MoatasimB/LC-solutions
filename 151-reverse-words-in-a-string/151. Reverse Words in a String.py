class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split()

        i = 0
        j = len(s_list) - 1

        while i <= j:
            if s_list[i] == " ":
                i += 1
                continue
            if s_list[j] == " ":
                j -= 1
                continue
            
            s_list[i], s_list[j] = s_list[j], s_list[i]

            i += 1
            j -= 1
        
        return " ".join(s_list)