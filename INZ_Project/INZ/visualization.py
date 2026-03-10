import matplotlib.pyplot as plt

def plot_gantt(timeline):
    fig, ax = plt.subplots()

    for pid, start, end in timeline:
        ax.barh(y=f"P{pid}", width=end-start, left=start)

    ax.set_xlabel("Time")
    ax.set_title("CPU Scheduling Gantt Chart")
    plt.show()