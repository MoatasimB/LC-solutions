class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rq = collections.deque()
        dq = collections.deque()
        n = len(senate)

        for i in range(n):
            if senate[i]=="R":
                rq.append(i)
            else:
                dq.append(i)
        
        while rq and dq:
            if rq[0] < dq[0]:

                n+=1
                rq.append(n)
            else:

                n+=1
                dq.append(n)
            rq.popleft()
            dq.popleft()
        
        if not rq:
            return "Dire"
        else:
            return "Radiant"

        