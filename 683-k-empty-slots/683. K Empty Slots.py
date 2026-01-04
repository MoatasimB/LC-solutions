class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        
        #need to know what day each bulb is turned on
        #we check in between first bulb and bulb k distance away that
        #every bulb in between them is lit up on a day after

        #get what days each bulb is lit on

        n = len(bulbs)
        days = [0] * n

        for day, bulb in enumerate(bulbs):
            days[bulb - 1] = day + 1
        
        l = 0
        r = l + k + 1
        ans = float("inf")
        while r < n:
            is_valid = True
            for i in range(l + 1, r):
                #check if this bulb is lit before the ends
                if days[i] < days[l] or days[i] < days[r]:
                    #move to next window
                    l = i
                    r = i + k + 1
                    is_valid = False
                    break
            
            if is_valid:
                ans = min(ans, max(days[l], days[r]))
                l = r
                r  = l + k + 1
        
        return ans if ans != float("inf") else -1

