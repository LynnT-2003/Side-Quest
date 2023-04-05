def activity_selection(start, end):
    n = len(end)
    activities = []
    i = 0
    
    # Sort the activities based on their end time in ascending order
    sorted_activities = sorted(range(n), key=lambda i: end[i])
    
    # Select the first activity and add it to the solution set
    activities.append(sorted_activities[0])
    last_finish_time = end[sorted_activities[0]]
    
    # Iterate over the remaining activities and add them to the solution set 
    # if their start time is larger than the finish time of the previous activity
    for j in range(1, n):
        # If the start time of the current activity is larger than the 
        # finish time of the previous activity, add it to the solution set
        if start[sorted_activities[j]] >= last_finish_time:
            activities.append(sorted_activities[j])
            last_finish_time = end[sorted_activities[j]]
    
    return activities

# Read input
n = int(input())
start = []
end = []
for i in range(n):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

# Apply activity selection algorithm and print the result
activities = activity_selection(start, end)
print(*activities)
