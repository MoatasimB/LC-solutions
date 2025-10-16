class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        gcds = {}
        def gcd(a,b):
            ogA, ogB = a, b
            if (a,b) in gcds:
                return gcds[(a,b)]
            while b:
                a, b = b, a % b
            gcds[(ogA,ogB)] = a
            return a
        
        def lcm(a,b):
            return abs(a * b) // gcd(a,b)
        
        stack = [nums[0]]

        def check():
            prev = stack[-1]
            curr = nums[i]

            gcd_nums = gcd(prev, curr)
            if gcd_nums > 1:
                stack.pop()

                new_num = lcm(prev, curr)
            return new_num
        i = 1
        while i < len(nums):
            new_num = nums[i]
            while stack:
                prev = stack[-1]
                curr = new_num
                # print(stack, prev, curr)

                gcd_nums = gcd(prev, curr)
                # print(gcd_nums)
                if gcd_nums > 1:
                    stack.pop()
                    new_num = lcm(prev, curr)
                    # print(new_num)
                    if not stack:
                        stack.append(new_num)
                        i+=1
                        break
                    else:
                        continue
                else:
                    stack.append(curr)
                    i+=1
                    break
        
        return stack
        # [6,4,3,2,7,6,2]

        # [12] prev = 12
        #     curr = 3
        #     new_num = 12


