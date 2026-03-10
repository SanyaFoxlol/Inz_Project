from .base import Scheduler
from collections import deque

class RoundRobinScheduler(Scheduler):
    def __init__(self, processes, quantum=2):
        super().__init__(processes)
        self.quantum = quantum

    def run(self):
        time = 0
        queue = deque(sorted(self.processes, key=lambda x: x.arrival_time))

        while queue:
            p = queue.popleft()

            if p.start_time is None:
                p.start_time = max(time, p.arrival_time)
                time = p.start_time

            exec_time = min(self.quantum, p.remaining_time)
            p.remaining_time -= exec_time
            start = time
            time += exec_time
            end = time

            self.timeline.append((p.pid, start, end))

            if p.remaining_time > 0:
                queue.append(p)
            else:
                p.finish_time = time

        return self.timeline