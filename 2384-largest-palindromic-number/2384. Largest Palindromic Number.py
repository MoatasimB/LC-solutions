class Solution:
    def largestPalindromic(self, num: str) -> str:

 
        nums = list(num)
        nums.sort(reverse = True)

        seen = set()

        final = ""
        for n in nums:
            if n in seen:
                seen.remove(n)
                final += n
            else:
                seen.add(n)
        
        ans = []    
        i=0
        while i<len(final):
            if final[i] != '0':
                break
            i+=1
        
        while i< len(final):
            ans.append(final[i])
            i+=1
        
        second_half = ans[::-1]

        nmax = ''
        if seen:
            for ch in seen:
                if ch > nmax:
                    nmax = ch
            ans.append(nmax)
        

        ans.extend(second_half)

        if not ans:
            return "0"
        return "".join(ans)
