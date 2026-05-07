class Job:

    def __init__(self, id, deadline, profit):

        self.id = id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs):

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Create empty slots
    slots = ['-'] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job in jobs:

        # Check slots from deadline to beginning
        for i in range(job.deadline - 1, -1, -1):

            if slots[i] == '-':

                slots[i] = job.id

                total_profit += job.profit

                break

    return slots, total_profit


# ---------------- USER INPUT ----------------

n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):

    print(f"\nEnter details for Job {i+1}")

    job_id = input("Enter Job ID: ")

    deadline = int(input("Enter Deadline: "))

    profit = int(input("Enter Profit: "))

    jobs.append(Job(job_id, deadline, profit))


# Function Call
result, profit = job_scheduling(jobs)

# Output
print("\nScheduled Jobs:", result)

print("Total Profit:", profit)
