class Solution:
    def countDistinct(self, n: int) -> int:
        #number of elements with no 0s

        str_n = str(n)
        x = len(str_n)

        # all numbers 1 digit less is just 9 + 9^2 + 9^3
        ans = 0
        for i in range(1, x):
            ans += 9**i
        
        #Now we want numbers from the same number of digits up to the number n ie if n=4594 we want all 4 digits with only non 0s less than n

        #we can break this apart to:
            #first digit we can do 1,2,3 (3 choices)
            #remaining digits is 9 choices each

            #next digit we repeat the process we can do 1 2 3 4 (4 choices)
            #remaining digits is 9 choicies each

            #what this simulates is getting all the numbers 1000s,2000s,3000s, 4100s, 4200s, 4300s, 4400s, 4510s, 4520s, ..., 4580s, 4591,4592,4593
            #then final check is number itself so

        for i, s in enumerate(str_n):
            digit = int(s)
            if digit == 0:
                break

            first_digit_choice = digit - 1

            ans += first_digit_choice * 9**(x-i-1) ##remaining places are 9 choices each
        if "0" not in str_n:
            ans += 1
        return ans


        # 4594

        # 3* 9^3
        # 4* 9^2
        # 8 * 9
        # 3

        # 4029

        

