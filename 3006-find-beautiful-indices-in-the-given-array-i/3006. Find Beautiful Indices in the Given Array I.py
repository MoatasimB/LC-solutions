class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        def find_matches(m, p): #main string, phrase
            ans = []
            if len(p) > len(m):
                return ans
            curr = 0
            for i in range(len(m) - len(p) + 1):
                if p[curr] == m[i]:
                    start = i

                    while curr < len(p) and start < len(m) and p[curr] == m[start]:
                        curr += 1
                        start += 1
                    
                    if curr == len(p):
                        ans.append(i)
                    
                    curr = 0

            return ans
        
        a_matches = find_matches(s, a)
        b_matches = find_matches(s, b)

        # a_matches.sort()
        # b_matches.sort()

        # [16, 33]
        # [4, 18]

        fin = []
        print(a_matches)
        print(b_matches)
        for i in range(len(a_matches)):
            for j in range(len(b_matches)):
                if abs(a_matches[i] - b_matches[j]) <= k:
                    fin.append(a_matches[i])
                    break
        
        return sorted(fin)

                




    