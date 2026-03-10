CPU Scheduling Simulator

This project is a Python-based CPU scheduling simulator that demonstrates and compares different process scheduling algorithms used in operating systems.

The program simulates how a CPU schedules processes and visualizes the execution timeline using a Gantt chart.

Features

Simulation of common CPU scheduling algorithms:

FCFS (First Come First Serve)

SJF (Shortest Job First)

Round Robin (RR)

Process timeline visualization (Gantt chart)

Calculation of important scheduling metrics:

Waiting time

Turnaround time

Command-line interface for selecting scheduling algorithms

Project Structure

INZ/
│
├── main.py                 # Main entry point of the program
├── process.py              # Process class definition
├── metrics.py              # Functions for calculating scheduling metrics
├── visualization.py        # Gantt chart visualization
│
└── schedulers/
    ├── base.py             # Base scheduler class
    ├── fcfs.py             # First Come First Serve implementation
    ├── sjf.py              # Shortest Job First implementation
    └── rr.py               # Round Robin implementation
Requirements

Python 3.8+

Required libraries:

matplotlib
Install dependencies:

pip install matplotlib
How to Run

Run the program from the project directory:

python main.py
Select Scheduling Algorithm

You can specify the algorithm using the --algo argument.

FCFS (default):

python main.py --algo fcfs

SJF:

python main.py --algo sjf

Round Robin:

python main.py --algo rr --quantum 2
Example Output

The program will:

Simulate the scheduling algorithm.

Display a Gantt chart showing process execution order.

Print the execution timeline.

Calculate and display scheduling metrics.

Example:

Timeline:
P1: 0 → 5
P2: 5 → 8
P3: 8 → 16
P4: 16 → 22

Metrics:
P1: waiting=0, turnaround=5
P2: waiting=4, turnaround=7
...
Sample Processes

The simulator uses predefined example processes:

Process	Arrival Time	Burst Time
P1	0	5
P2	1	3
P3	2	8
P4	3	6

These can be modified in main.py.

Educational Purpose

This project is designed for learning and demonstrating CPU scheduling algorithms used in operating systems courses.

It helps visualize how different algorithms affect:

process waiting time

turnaround time

CPU scheduling order

If you want, I can also make a more "student-looking" README (simpler, like universities expect) or a more professional GitHub-style README with screenshots and badges.
