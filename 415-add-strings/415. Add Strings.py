class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        n1 = len(num1)
        n2 = len(num2)

        i = n1 - 1
        j = n2 - 1
        carry = 0

        ans = []

        while i >= 0 and j >= 0:

            s = (int(num1[i]) + int(num2[j]) + carry) % 10
            carry = (int(num1[i]) + int(num2[j]) + carry) // 10

            ans.append(str(s))

            i-=1
            j-=1
        

        while i >= 0:
            s = (int(num1[i]) + carry) % 10
            carry = (int(num1[i]) + carry) // 10
            ans.append(str(s))
            i -= 1
        
        while j >= 0:
            s = (int(num2[j]) + carry) % 10
            carry = (int(num2[j]) + carry) // 10
            ans.append(str(s))
            j -= 1
        
        if carry:
            ans.append('1')
        

        return "".join(ans[::-1])
            


