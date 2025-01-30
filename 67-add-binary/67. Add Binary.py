class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            s = carry + int(a[i]) + int(b[j])

            if s == 3:
                carry = 1
                s = 1
            elif s == 2:
                carry = 1
                s = 0
            elif s == 1:
                carry = 0
                s = 1
            ans.append(str(s))
            i -= 1
            j -= 1
        while i >= 0: 
            s = carry + int(a[i])

            if s == 2:
                carry = 1
                s = 0
            elif s == 1:
                carry = 0
                s = 1
            ans.append(str(s))
            i -= 1

        while j >= 0: 
            s = carry + int(b[j])

            if s == 2:
                carry = 1
                s = 0
            elif s == 1:
                carry = 0
                s = 1
            ans.append(str(s))
            j -= 1

        if carry:
            ans.append(str(1))
        
        ans.reverse()

        return "".join(ans)
