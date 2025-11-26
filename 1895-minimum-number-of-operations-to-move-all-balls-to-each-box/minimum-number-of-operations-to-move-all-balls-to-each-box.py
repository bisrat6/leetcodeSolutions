from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # Left-to-right pass: cost to bring balls from the left side to current i
        balls = 0
        moves = 0
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        # Right-to-left pass: cost to bring balls from the right side to current i
        balls = 0
        moves = 0
        for i in range(n-1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        return answer
