class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        n = len(heights)

        for _ in range(volume):
            place_left = False
            place_right = False
            curr = heights[k]

            lowest = float("inf")
            left_side = {} #height : idx
            for i in range(k, -1, -1):
                if heights[i] not in left_side:
                    left_side[heights[i]] = i
                if heights[i] < lowest:
                    lowest = heights[i]
                if i - 1 >= 0 and heights[i - 1] > heights[i]:
                    break
                
            print("leftside", left_side, lowest)

            
            if lowest < curr:
                place_left = True

            if place_left == True:
                heights[left_side[lowest]] += 1
                print(heights)
                continue
            

            lowest = float("inf")
            right_side = {}
            for i in range(k, n):
                if heights[i] not in right_side:
                    right_side[heights[i]] = i
                
                if heights[i] < lowest:
                    lowest = heights[i]
                if i + 1 < n and heights[i] < heights[i + 1]:
                    break
            print("rightSide", right_side, lowest)

            print()
            if lowest < curr:
                place_right = True
            
            if place_right == True:
                heights[right_side[lowest]] += 1
                print(heights)
                continue
            
            heights[k] += 1
        
        return heights
            

        [4,4,4,4,3,2,1,2,3,4,3,2,1]

        [1,2,3,4,3,2,1,2,3,4,3,2,1]