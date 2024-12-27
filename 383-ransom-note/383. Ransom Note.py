class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        ransomDic = defaultdict(int)
        for ch in ransomNote:
            ransomDic[ch] +=1
        
        magDic = defaultdict(int)
        for ch in magazine:
            magDic[ch] +=1
        
        for key, val in ransomDic.items():
            if magDic[key] < val:
                return False

        return True