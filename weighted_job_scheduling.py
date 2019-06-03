"""
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated
Find the maximum profit subset of jobs such that no two jobs in the subset
overlap.

Input: Number of Jobs n = 4
   Job Details {Start Time, Finish Time, Profit}
   Job 1:  {1, 2, 50}
   Job 2:  {3, 5, 20}
   Job 3:  {6, 19, 100}
   Job 4:  {2, 100, 200}

Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3
but the profit with this schedule is 20+50+100 which is less than 250.
"""
jobs = [[1, 2, 50], [3, 5, 20], [4, 19, 100], [12, 20, 150], [2, 100, 200]]

def find_max_profit(jobs):
    # sort jobs by end time, earliest to latest
    jobs.sort(key=lambda j: j[1])

    max_profit = 0

    # ensure i and j are different, so we can compare different tasks
    # if both i and j started at 0, we're basically just looking at one task
    i = 1
    while i < len(jobs):
        i_start, i_end, profit = jobs[i]
        j = 0
        while j < i:
            j_start, j_end, j_profit = jobs[j]
            if j_start >= i_end or j_end <= i_start:  # if there is no overlap
                profit += j_profit
            j += 1
        # update max_profit as we go through
        max_profit = max(max_profit, profit)
        i += 1
    return max_profit

print(find_max_profit(jobs) == 250)