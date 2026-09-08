class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        students = defaultdict(list)

        for student, score in items:
            heapq.heappush(students[student], score)
            if len(students[student]) > 5:
                heapq.heappop(students[student])
        
        ans = []
        for student, scores in students.items():
            ans.append([student, sum(scores) // 5])
        
        ans.sort()
        return ans