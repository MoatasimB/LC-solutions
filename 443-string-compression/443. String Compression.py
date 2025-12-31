class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ans = []

        prev = None
        curr = 0
        i = 0

        j = 0

        while i < len(chars):
            if not prev:
                prev = chars[i]
                curr = 1
            elif prev and (chars[i] != prev):
                if curr == 1:
                    chars[j] = prev
                    j += 1
                else:
                    chars[j] = prev
                    j += 1
                    for ch in str(curr):
                        chars[j] = ch
                        j += 1


                prev = chars[i]
                curr = 1
            else:
                curr += 1
            
            i += 1
        
        chars[j] = prev
        if curr == 1:
            j += 1
        else:
            j += 1
            for ch in str(curr):
                chars[j] = ch
                j += 1

        return j
