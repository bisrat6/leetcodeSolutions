class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # 0-indexed winner when there's 1 person
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1  # convert to 1-indexed
