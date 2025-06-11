class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return n == 0 if flowerbed[0] == 1 else n == 1 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0 and i < len(flowerbed) - 1:
                if flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i > 0 and i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i+ 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            
            if n == 0:
                return True
        
        return False