class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        carry = 1

        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry

            if digits[i] >= 10:
                digits[i] = digits[i] % 10
            else:
                carry = 0
                break

        if digits[0] >= 10 or carry:
            digits[0] = digits[0] % 10
            return [1] + digits 
        else:
            return digits           

