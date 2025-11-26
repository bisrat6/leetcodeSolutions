from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        dq = deque()
        # build the deck in reverse
        for card in reversed(sorted_deck):
            if dq:
                # move bottom card to top (reverse of the reveal-process's move-to-bottom)
                dq.appendleft(dq.pop())
            # put the current (largest‑remaining) card on top
            dq.appendleft(card)
        return list(dq)
