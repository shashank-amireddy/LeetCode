class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        cnt = 0
        l = len(flowerbed)

        for i in range(l):
            if flowerbed[i] == 0:
                is_left = (i == 0) or (flowerbed[i - 1] == 0)
                is_right = (i == l - 1) or (flowerbed[i + 1] == 0)

                if is_left and is_right:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt >= n:
                        return True
        return cnt >= n
