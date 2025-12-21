class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        squares = [[bottomLeft[i], topRight[i]] for i in range(n)]
        #[[[1, 1], [5, 5]], ]
        squares.sort(key = lambda x : x[0])
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                squareOneBottom = squares[i][0]
                squareOneTop = squares[i][1]

                squareTwoBottom = squares[j][0]
                squareTwoTop = squares[j][1]

                if not (squareTwoBottom[0] > squareOneTop[0] or squareTwoBottom[1] > squareOneTop[1]):

                    # print(squareOneBottom, squareOneTop,squareTwoBottom, squareTwoTop)
                    #bottomLeft
                    a, b = squareOneBottom
                    c, d = squareTwoBottom
                    bottomLeft = [max(a, c), max(b,d)]

                    

                    #topRight
                    a, b = squareOneTop
                    c, d = squareTwoTop
                    topRight = [min(a, c), min(b,d)]

                  

                    topRightX, topRightY = topRight
                    bottomLeftX, bottomLeftY = bottomLeft

                    #can Intersect
                    y_diff = topRightY - bottomLeftY

                    x_diff = topRightX - bottomLeftX

                    side = max(0, min(y_diff, x_diff))
                    
                    ans = max(ans, side**2)

            
        
        return ans

