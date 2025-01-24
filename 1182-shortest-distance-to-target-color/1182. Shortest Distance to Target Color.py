class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        colorsInArray = set(colors)

        ans = []
        dp = {}
        for idx in range(len(queries)):
            i,c = queries[idx]
            if c not in colorsInArray:
                ans.append(-1)
            if (i,c) in dp:
                ans.append(dp[(i,c)])
                continue
            
            left = i
            right = i

            while left >= 0 and right < len(colors):
                if colors[left] == c:
                    ans.append(i - left)
                    break
                if colors[right] == c:
                    ans.append(right - i)
                    break
                
                left -= 1
                right +=1
            if len(ans) == idx+1:
                dp[(i,c)] = ans[-1]
                continue
            while left >= 0:
                if colors[left] == c:
                    ans.append(i - left)
                    break
                left -= 1
            
            while right < len(colors):
                if colors[right] == c:
                    ans.append(right - i)
                    break
                right += 1
            dp[(i,c)] = ans[-1]
        return ans