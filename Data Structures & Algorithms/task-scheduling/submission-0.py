class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = [-c for c in count.values()]
        heapq.heapify(count)
        q = deque()
        time = 0

        while q or count:
            time += 1
            if count:
                cnt = 1 + heapq.heappop(count)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(count, q.popleft()[0])
        return time