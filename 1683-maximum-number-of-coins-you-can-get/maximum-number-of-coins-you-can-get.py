from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        # we will pick n = len(piles)//3 piles for us
        # we sum every second‑largest in the top 2n piles
        # that corresponds to indices: len(piles) - 2, len(piles) - 4, ..., len(piles) - 2n
        n = len(piles) // 3
        for i in range(1, n + 1):
            res += piles[-2 * i]
        return res
