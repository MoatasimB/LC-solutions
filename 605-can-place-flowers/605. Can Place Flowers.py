class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):

            if flowerbed[i] == 1:
                continue
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
            if left and right:
                n -= 1
                flowerbed[i] = 1 

                if n == 0:
                    return True
        
        return False


