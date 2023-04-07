def minimize_lateness(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task[1])

    current_time = 0
    max_lateness = 0
    task_order = []

    for task in sorted_tasks:
        duration, deadline = task
        current_time += duration
        lateness = max(current_time - deadline, 0)
        max_lateness = max(max_lateness, lateness)
        task_order.append(tasks.index(task))

    return task_order, max_lateness

# Read input
n = int(input())
tasks = []
for i in range(n):
    s, e = map(int, input().split())
    tasks.append((s, e))

task_order, max_lateness = minimize_lateness(tasks)
print(' '.join(map(str, task_order)))
print(max_lateness)
