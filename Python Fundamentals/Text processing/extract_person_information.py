n = int(input())

for i in range(n):
    inp = input()

    name_start_index = inp.find('@')
    name_end_index = inp.find('|')
    name = inp[name_start_index + 1: name_end_index]

    age_start_index = inp.find('#')
    age_end_index = inp.find('*')
    age = inp[age_start_index + 1: age_end_index]

    print(f"{name} is {age} years old.")
