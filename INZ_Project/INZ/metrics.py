def calculate_metrics(processes):
    results = []
    for p in processes:
        turnaround = p.finish_time - p.arrival_time
        waiting = turnaround - p.burst_time
        results.append((p.pid, waiting, turnaround))
    return results