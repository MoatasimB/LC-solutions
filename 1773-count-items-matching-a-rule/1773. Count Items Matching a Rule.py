class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for t, c, n in items:
            if ruleKey == 'type' and t == ruleValue:
                ans +=1
            elif ruleKey == 'color' and c == ruleValue:
                ans +=1
            elif ruleKey == 'name' and n == ruleValue:
                ans +=1
        
        return ans

