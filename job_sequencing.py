"""
Given an array of jobs where every job has a deadline and associated profit if
the job is finished before the deadline. It is also given that every job takes
single unit of time, so the minimum possible deadline for any job is 1. How to
maximize total profit if only one job can be scheduled at a time.

Input: Four Jobs with following deadlines and profits:
JobID  Deadline  Profit
  a      4        20
  b      1        10
  c      1        40
  d      1        30
Output: Following is maximum
profit sequence of jobs
    c, a


Input:  Five Jobs with following deadlines and profits:
JobID   Deadline  Profit
  a       2        100   [0, 1, 2]
  b       1        19    [0, 1]
  c       2        27    [0, 1, 2]
  d       1        25    [0, 1]
  e       3        15
Output: Following is maximum
profit sequence of jobs
    c, a, e
"""

def get_maximum_profit_sequence(jobs):
    # sort jobs by profit (highest to lowest)
    jobs.sort(key=lambda j: j[2], reverse=True)
    max_deadline = max(jobs, key=lambda j: j[1])[1]
    sequence = [None for _ in xrange(max_deadline)]
    total_profit = 0
    for job in jobs:
        name, deadline, profit = job
        pos = deadline - 1
        if not sequence[pos]:
            sequence[pos] = name
            total_profit += profit
        else:
            while sequence[pos]:
                pos -= 1
            if pos > -1:
                sequence[pos] = name
                total_profit += profit
    return list(filter(None, sequence))

jobs1 = [('a', 4, 20), ('b', 1, 10), ('c', 1, 40), ('d', 1, 30)]
res1 = ['c', 'a']

jobs2 = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
res2 = ['c', 'a', 'e']

print(get_maximum_profit_sequence(jobs1) == res1)
print(get_maximum_profit_sequence(jobs2) == res2)