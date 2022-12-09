chemical_elements = set()

for _ in range(int(input())):
    elements = input().split()
    for element in elements:
        chemical_elements.add(element)

print(*chemical_elements, sep='\n')
