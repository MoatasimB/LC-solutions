class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def transform(x):

            mpp = {}
            id = 0
            ans = []
            for ch in x:
                if ch not in mpp:
                    mpp[ch] = str(id)
                    ans.append(mpp[ch])
                    id +=1
                else:
                    ans.append(mpp[ch])
            # print(ans)
            
            return " ".join(ans)
        
        return transform(s) == transform(t)
