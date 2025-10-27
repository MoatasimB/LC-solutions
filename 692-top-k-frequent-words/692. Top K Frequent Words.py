class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        lst = []

        for word, count in freq.items():
            heapq.heappush(lst, [count, word])
            # if len(lst) > k:
            #     heapq.heappop(lst)
        
        lst.sort(key= lambda x: (-x[0], x[1]))

        # new_lst.sort(key = lambda x: (x[0], x[1]), reverse = True)

        
        return [w for c, w in lst[:k]]