class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        ans = []
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i][0], slots1[i][1]
            start2, end2 = slots2[j][0], slots2[j][1]

            beg = max(start1, start2)
            fin = min(end1, end2)

            if fin - beg >= duration:
                return [beg, beg + duration]

   
            else:
                if end2 < end1:
                    j +=1
                else:
                    i+=1
        return []



