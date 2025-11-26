from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        # add the new request timestamp
        self.q.append(t)
        # remove outdated timestamps
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        # number of valid recent calls
        return len(self.q)
