class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        words.sort()
        ans = []
        for top in words:
            for left in words:
                if left == top:
                    continue
                for right in words:
                    if right == top or right == left:
                        continue
                    for bottom in words:
                        if bottom == top or bottom == left or bottom == right:
                            continue

                        if top[0] == left[0] and top[3] == right[0] and bottom[0] == left[3] and bottom[3] == right[3]:
                            ans.append([top, left, right, bottom])

        return ans
                        