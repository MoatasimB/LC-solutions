class Solution:
    def robotWithString(self, s: str) -> str:

        t = []
        answer = []
        counts = defaultdict(int)

        for c in s:
            counts[c] +=1
        
        for c in s:
            t.append(c)

            counts[c] -=1
            if counts[c] == 0:
                del counts[c]
        
            while t and (not counts or t[-1]<= min(counts.keys())):
                answer.append(t.pop())

        return "".join(answer)

        