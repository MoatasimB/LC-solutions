class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        counts = defaultdict(int)

        if len(hand) % groupSize != 0:
            return False
        
        for n in hand:
            counts[n] += 1
        
        hand.sort()
        print(hand)
        i = 0

        while i < len(hand):
            start = hand[i]
            if counts[start] <= 0:
                i += 1
                continue
            counts[start] -= 1
            print(start)
            print("-------")
            for _ in range(groupSize-1):
                if start + 1 in counts and counts[start + 1] > 0:
                    start += 1
                    counts[start] -= 1
                else:
                    print(start, counts[start + 1])
                    return False
            i+=1
        
        return True