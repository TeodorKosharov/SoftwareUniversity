population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())
is_distribution_possible = False

for index in range(len(population)):

    if population[index] < minimum_wealth:
        diff = minimum_wealth - population[index]
        population[index] += diff
        wealthiest = max(population)
        wealthiest_index = population.index(wealthiest)
        population[wealthiest_index] -= diff

for number in population:
    if number < minimum_wealth:
        is_distribution_possible = False
        break
    else:
        is_distribution_possible = True

if is_distribution_possible:
    print(population)
else:
    print("No equal distribution possible")
