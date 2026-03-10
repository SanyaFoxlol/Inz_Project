from abc import ABC, abstractmethod

class Scheduler(ABC):
    def __init__(self, processes):
        self.processes = processes
        self.timeline = []

    @abstractmethod
    def run(self):
        pass