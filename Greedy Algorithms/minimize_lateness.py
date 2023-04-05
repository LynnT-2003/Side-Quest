def minimize_lateness(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task[1])

    current_time = 0
    lateness = [0] * len(tasks)
    task_order = [0] * len(tasks)
    max_lateness = 0

    for i in range(len(sorted_tasks)):
        task = sorted_tasks[i]
        index = tasks.index(task)
        task_order[i] = index
        current_time += task[0]
        lateness[i] = max(0, current_time - task[1])
        max_lateness = max(max_lateness, lateness[i])

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
