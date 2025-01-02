class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        #For the senators to win they want to keep banning the next senator
        #This game could be simulated by seperating the two groups of senator
        #Then we put them head to head one at a time
        #The senator who came first in the original list wins that round and is moved to back 
        #Of their own list with an updated number
        #This simulates he is in the next round with his new number
        #We continue this game till one of the senator lists are empty

        #The data structure for this would be a q as we need to popfrom the left and 
        #put them back on their q

        rq = deque()
        dq = deque()
        n = len(senate)

        #Since I am appending each to their respective q I will only append their position
        #Their position is how I determine who wins as lower position bans higher position
        for i in range(len(senate)):
            if senate[i] =="R":
                rq.append(i)
            else:
                dq.append(i)
        
        #now I keep making them face off till one of their q are empty
        while rq and dq:
            #I check who came first in the list cause this determins who wins
            if dq[0] < rq[0]:
                #If dq did then we put this senator back on its own q with an updated number
                dq.append(n)
                #Then we udpate n for the next senator
                n+=1
            else:
                rq.append(n)
                n+=1
            #regardless we popoff these senators because the winner got to move on
            dq.popleft()
            rq.popleft()
        
        if not rq:
            return "Dire"
        else:
            return "Radiant"