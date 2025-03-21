class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        def decode(arr):
            ans = []
            for i in range(len(arr)):
                num, freq = arr[i]
                for _ in range(freq):
                    ans.append(num)
            return ans
        
        def encode(arr):
            i = 0
            ans = []
            while i < len(arr) - 1:
                curr_num = arr[i]
                count = 0
                while i < len(arr) - 1 and arr[i] == arr[i+1]:
                    count += 1
                    i += 1
                ans.append([curr_num, count])
            if not ans:
                return []
            last_num = ans[-1][0]
            if last_num == arr[i]:
                ans[-1][1] += 1
            else:
                ans.append([arr[i], 1])
            return ans
                
        # decoded1 = decode(encode1)
        # decoded2 = decode(encode2)
        
        i = 0
        j = 0
        ans = []
        while i < len(encoded1) and j < len(encoded2):
            num1, f1 = encoded1[i]
            num2, f2 = encoded2[j]

            new_num = num1 * num2
            count = min(f1, f2)
            if ans and ans[-1][0] == new_num:
                ans[-1][1] += count
            else:
                ans.append([new_num, count])

            f1 -= count
            f2 -= count

            if f1 == 0:
                i += 1
            else:
                encoded1[i][1] = f1
            if f2 == 0:
                j += 1
            else:
                encoded2[j][1] = f2
            
        return ans
        


