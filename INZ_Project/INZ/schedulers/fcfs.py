from .base import Scheduler

class FCFSScheduler(Scheduler):
    def run(self):
        time = 0
        for p in sorted(self.processes, key=lambda x: x.arrival_time):
            if time < p.arrival_time:
                time = p.arrival_time

            p.start_time = time
            time += p.burst_time
            p.finish_time = time

            self.timeline.append((p.pid, p.start_time, p.finish_time))

        return self.timeline