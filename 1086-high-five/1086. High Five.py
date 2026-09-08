class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        

        table = defaultdict(list)

        for student, score in items:
            table[student].append(score)

        ans = []
        for key, val in table.items():
            val.sort(reverse=True)
            print(val)

            s = 0
            for x in range(5):
                s += val[x]
            avg = s//5
            ans.append([key, avg])
        
        
        ans.sort(key=lambda x: x[0])
        return ans