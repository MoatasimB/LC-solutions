class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        carry = 0
        padding = 1
        total = 0
        paddingj=1
        for j in range(len(num2)-1, -1, -1):
            paddingi = 1
            curr = 0
            for i in range(len(num1)-1, -1, -1):
                curr += (int(num1[i]) * paddingi) * (int(num2[j]) * paddingj)
               
                paddingi *=10
            total +=curr
            paddingj *=10
        
        return str(total)
        