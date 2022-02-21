data = []

# We create nested lists containing the data of all pipes:
for i in range(int(input())):
    data.append(list(map(int, input().split())))

best_pipe_index = 0
is_cycle_completed = False

# Iterating until we find the best pipe (the pipe from which we will be able to complete the cycle):
while True:
    current_petrol = 0
    start_pipe_index = best_pipe_index

    for _ in range(len(data) + 1):   # len(data) + 1 = x; after x iterations we will finish at the pipe we started from (completed cycle)
        if start_pipe_index == len(data):
            start_pipe_index = 0

        current_petrol += data[start_pipe_index][0]
        distance = data[start_pipe_index][1]
        current_petrol -= distance
        if current_petrol < 0:      # run out of petrol - break the loop and start checking the next pipe
            best_pipe_index += 1
            is_cycle_completed = False
            break
        else:
            is_cycle_completed = True
        start_pipe_index += 1

    if is_cycle_completed:
        print(best_pipe_index)
        exit()
