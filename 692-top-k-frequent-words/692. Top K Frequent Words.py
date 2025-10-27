class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class Node:
            def __init__(self, count, word):
                self.count = count
                self.word = word
            
            def __lt__(self, other):
                if self.count != other.count:
                    return self.count < other.count
                return self.word > other.word

        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        lst = []

        for word, count in freq.items():
            heapq.heappush(lst, Node(count, word))
            if len(lst) > k:
                heapq.heappop(lst)
        
        # lst.sort(key= lambda x: (-x[0], x[1]))

        # new_lst.sort(key = lambda x: (x[0], x[1]), reverse = True)

        lst.sort(reverse = True)
        return [p.word for p in lst]