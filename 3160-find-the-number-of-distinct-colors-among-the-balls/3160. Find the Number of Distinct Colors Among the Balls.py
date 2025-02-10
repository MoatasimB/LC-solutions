class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        color_of_ball = {}

        balls_of_this_color = defaultdict(set)
        ans = []
        for ball, color in queries:
            curr = None
            if ball in color_of_ball:
                curr = color_of_ball[ball]
            color_of_ball[ball] = color
            balls_of_this_color[color].add(ball)
            if curr and curr != color:
                balls_of_this_color[curr].remove(ball)

            if len(balls_of_this_color[curr]) == 0:
                del balls_of_this_color[curr]
            ans.append(len(balls_of_this_color))
        
        return ans