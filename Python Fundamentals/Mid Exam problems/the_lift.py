waiting_ppl = int(input())
lift_state = list(map(int, input().split()))

for index in range(len(lift_state)):
    current_state = lift_state[index]
    ppl_to_join = 4 - current_state
    if waiting_ppl < ppl_to_join:
        ppl_to_join = waiting_ppl
    waiting_ppl -= ppl_to_join
    lift_state[index] += ppl_to_join

if waiting_ppl > 0:
    print(f"There isn't enough space! {waiting_ppl} people in a queue!")
    print(' '.join(list(map(str, lift_state))))

elif lift_state.count(4) == len(lift_state) and waiting_ppl == 0:
    print(' '.join(list(map(str, lift_state))))

else:
    print("The lift has empty spots!")
    print(' '.join(list(map(str, lift_state))))
