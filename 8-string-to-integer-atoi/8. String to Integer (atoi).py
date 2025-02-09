class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.split()
        if not s:
            return 0
        
        num = s[0]
        negative = False
        if num[0] == '-':
            negative = True
            num = num[1:]
        elif num[0] == '+':
            num = num[1:]
        
        ans = 0
        curr_num = []

        for i in range(len(num)):
            if num[i] not in '0123456789':
                break
            else:
                curr_num.append(int(num[i]))
        print(curr_num)
        power = 0

        for i in range(len(curr_num)-1, -1, -1):
            ans += 10**power * curr_num[i]
            power +=1
        if negative:
            ans = -ans
        if ans > 2**31 - 1:
            return 2**31 - 1
        if ans < -(2**31):
            return -(2**31)
        return ans

