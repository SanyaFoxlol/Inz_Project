from dataclasses import dataclass

@dataclass
class Process:
    pid: int
    arrival_time: int
    burst_time: int
    priority: int = 0

    remaining_time: int = None
    start_time: int = None
    finish_time: int = None

    def __post_init__(self):
        self.remaining_time = self.burst_time

