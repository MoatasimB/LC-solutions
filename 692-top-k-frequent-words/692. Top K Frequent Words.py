class Node:
    def __init__(self,count,value):
        self.count = count
        self.value = value
    def __lt__ (self, other):
        if self.count != other.count:
            return self.count < other.count
        return self.value > other.value
class Solution:

    #Easy to solve this in nlogn with a max heap but need min heap for nlogk

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        heap = []
        count = defaultdict(int)

        for word in words:
            count[word] +=1
        
        for key,val in count.items():
            heapq.heappush(heap, Node(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
            
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).value)

        final = []
        for i in range(len(ans) - 1, -1, -1):
            final.append(ans[i])
        
        return final

        # while heap:
        #     ans.append(heappop(heap))

        # ans.sort(key=lambda x: (-x[0], -x[1], x[2])) #sort by smallest neg and then lexo order

        # return [word1 for freq, word, word1 in ans]
        