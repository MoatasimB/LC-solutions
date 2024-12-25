class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1


        while left< right:
            while s[left].isalnum() == False and left < right:
                left +=1
                # if left > len(s) - 1:
                #     return True
            while s[right].isalnum() == False and left < right:
                right -= 1
                # if right < 0:
                #     return True

            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -=1

        return True