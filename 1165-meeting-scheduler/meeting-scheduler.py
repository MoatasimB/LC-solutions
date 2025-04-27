class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]

            if end1 < start2:
                i += 1
                continue
            if end2 < start1:
                j += 1
                continue
            
            beg = max(start1, start2)
            end = min(end1, end2)

            if end - beg >= duration:
                return [beg, beg + duration]
            
            if end1 < end2:
                i += 1
            else:
                j += 1
            # i += 1
            # j += 1
        
        return []

    #    ------------------------------------
    #      ---------         