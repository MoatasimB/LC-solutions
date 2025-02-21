class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ans = []
        while i >= 0 and j >= 0:
            curr = int(num1[i]) + int(num2[j]) + carry
            digit = curr % 10
            ans.append(str(digit))
            if curr >= 10:
                carry = 1
            else:
                carry = 0
            i -=1
            j -= 1
        while j >= 0:
            curr = carry + int(num2[j])
            digit = curr % 10
            ans.append(str(digit))
            if curr >= 10:
                carry = 1
            else:
                carry = 0
            j -=1
        while i >= 0:
            curr = carry + int(num1[i])
            digit = curr % 10
            ans.append(str(digit))
            if curr >= 10:
                carry = 1
            else:
                carry = 0
            i -=1
        if carry:
            ans.append(str(carry))

        i = 0
        j = len(ans) - 1
        while i <= j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
        print(ans)
        return "".join(ans)
       



