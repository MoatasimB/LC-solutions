class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        curr1 = [0] * len(s)
        curr = [0] * len(s)

        for i in range(len(s)):
            curr1[i] = ord(s[i]) - ord('a')
        
        for start, end, direction in shifts:
            if direction == 0:
                curr[start] -=1
                if end + 1 < len(s):
                    curr[end+1] +=1

            else:
                curr[start] +=1
                if end + 1 < len(s):
                    curr[end+1] -=1

        for i in range(1, len(curr)):
            curr[i] = (curr[i] + curr[i-1])
        

        for i in range(len(curr)):
            curr1[i] += (curr[i])
            curr1[i] %= 26

        for i in range(len(curr1)):
            curr1[i] = (chr(abs((curr1[i] + 97))))


        return "".join(curr1)