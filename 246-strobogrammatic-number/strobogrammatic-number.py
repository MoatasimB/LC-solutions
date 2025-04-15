class Solution:
    def isStrobogrammatic(self, num: str) -> bool:


        for i in range(len(num)):
            if num[i] in "23457":
                return False
        mpp = {"6" : "9",
                "9" :"6",
                "8" : "8",
                "1" : "1",
                "0" : "0"     
                        }
        new_num = []
        for i in range(len(num)):
            new_num.append(mpp[num[i]])
       
        return int("".join(new_num)[::-1]) == int(num)