class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        

        ans = ""
        for i in range(len(str2)):
            curr = str1.split(f"{str2[:i+1]}")
            curr2 = str2.split(f"{str2[:i+1]}")
            flag = True
            for el in curr:
                if el:
                    flag = False
                    break
            for el in curr2:
                if el:
                    flag = False
                    break
            if flag:
                ans = str2[:i+1]
        
        return ans