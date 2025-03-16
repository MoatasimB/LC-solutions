class Solution:
    def maximumSwap(self, num: int) -> int:
        
        str_num = list(str(num))

        nextLargest = [0] * len(str_num)
        nextLargest[-1] = len(str_num) - 1
        
        for i in range(len(str_num)-2, -1, -1):
            if int(str_num[nextLargest[i+1]]) >= int(str_num[i]):
                nextLargest[i] = nextLargest[i+1]
            else:
                nextLargest[i] = i
        
        
        
        print(nextLargest)
        for i in range(len(str_num)):
            if int(str_num[i]) < int(str_num[nextLargest[i]]):
                str_num[i], str_num[nextLargest[i]] = str_num[nextLargest[i]],str_num[i]
            

                return int("".join(str_num))
        return num
