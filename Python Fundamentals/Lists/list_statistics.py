n = int(input())

positives_list = []
negatives_list = []

positives_count = 0
negatives_sum = 0

for i in range(n):

    value = int(input())

    if value >= 0:
        positives_list.append(value)
        positives_count += 1

    else:
        negatives_list.append(value)
        negatives_sum += value

print(positives_list)
print(negatives_list)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")
