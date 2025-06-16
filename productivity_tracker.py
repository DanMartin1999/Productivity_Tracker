
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Create or append productivity log
def log_task(task, duration):
    date = datetime.today().strftime('%Y-%m-%d')
    entry = pd.DataFrame([[date, task, duration]], columns=["Date", "Task", "Duration (hrs)"])
    if os.path.exists("productivity_log.csv"):
        entry.to_csv("productivity_log.csv", mode='a', header=False, index=False)
    else:
        entry.to_csv("productivity_log.csv", index=False)

# Summarize and visualize
def show_summary():
    df = pd.read_csv("productivity_log.csv")
    summary = df.groupby("Task")["Duration (hrs)"].sum()
    print("\nTotal Hours Spent Per Task:")
    print(summary)
    summary.plot(kind='bar', title='Total Hours Spent per Task')
    plt.ylabel('Total Hours')
    plt.tight_layout()
    plt.savefig("summary_chart.png")
    plt.show()

# Example usage:
if __name__ == "__main__":
    print("Welcome to the Productivity Tracker")
    while True:
        choice = input("Log new task (L), Show Summary (S), or Quit (Q)? ").strip().upper()
        if choice == "L":
            task = input("Enter task name (e.g., Study, Code): ")
            duration = float(input("Enter duration in hours: "))
            log_task(task, duration)
        elif choice == "S":
            show_summary()
        elif choice == "Q":
            break
        else:
            print("Invalid option.")
