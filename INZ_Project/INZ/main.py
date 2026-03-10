import argparse
from process import Process
from visualization import plot_gantt
from schedulers.fcfs import FCFSScheduler
from schedulers.sjf import SJFScheduler
from schedulers.rr import RoundRobinScheduler
from metrics import calculate_metrics

def sample_processes():
    return [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6),
    ]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", choices=["fcfs", "sjf", "rr"], default="fcfs")
    parser.add_argument("--quantum", type=int, default=2)
    args = parser.parse_args()

    processes = sample_processes()

    if args.algo == "fcfs":
        scheduler = FCFSScheduler(processes)
    elif args.algo == "sjf":
        scheduler = SJFScheduler(processes)
    else:
        scheduler = RoundRobinScheduler(processes, quantum=args.quantum)

    timeline = scheduler.run()
    plot_gantt(timeline)

    print("\nTimeline:")
    for t in timeline:
        print(f"P{t[0]}: {t[1]} → {t[2]}")

    print("\nMetrics:")
    for pid, wait, turn in calculate_metrics(processes):
        print(f"P{pid}: waiting={wait}, turnaround={turn}")

if __name__ == "__main__":
    main()