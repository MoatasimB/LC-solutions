class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
            ]
        ans = []
        for v,s in arr:
            if num == 0:
                break
            
            q = num // v
            r = num % v
            num = r

            ans.append(s*q)
        
        return "".join(ans)