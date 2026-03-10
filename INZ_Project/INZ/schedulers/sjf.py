from .base import Scheduler

class SJFScheduler(Scheduler):
    def run(self):
        time = 0
        processes = self.processes[:]
        completed = []

        while processes:
            available = [p for p in processes if p.arrival_time <= time]
            if not available:
                time += 1
                continue

            p = min(available, key=lambda x: x.burst_time)
            p.start_time = time
            time += p.burst_time
            p.finish_time = time

            self.timeline.append((p.pid, p.start_time, p.finish_time))
            processes.remove(p)
            completed.append(p)

        return self.timeline