jobs = list(map(int, input().split(', ')))
job_index = int(input())

jobs_indices = []
cycles = 0

sorted_jobs = sorted(jobs, reverse=True)

while True:
    min_value = min(sorted_jobs)
    sorted_jobs.pop()
    for index in range(len(jobs)):
        if jobs[index] == min_value and index not in jobs_indices:
            cycles += jobs[index]
            jobs_indices.append(index)

            if index == job_index:
                print(cycles)
                exit(0)
            break
