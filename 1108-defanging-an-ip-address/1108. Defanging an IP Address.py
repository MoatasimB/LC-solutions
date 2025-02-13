class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        lst = address.split('.')

        ans = []

        for el in lst:
            ans.append(el)
            ans.append("[.]")
        
        return "".join(ans[:len(ans) - 1])