# from math import ceil
#
# string = input().split()
# factor = int(input())
#
# happines = list(map(int, string))
#
# increased_happines = [value * factor for value in happines]
#
# elements = len(increased_happines)
# suma = 0
#
# for element in increased_happines:
#     suma += element
#
# average = suma / elements
# half_employees = int(elements / 2)
# unhappy = 0
#
# for element in increased_happines:
#
#     if element < average:
#         unhappy += 1
#
# if half_employees >= unhappy:
#     print(f"Score: {len(increased_happines) - unhappy}/{len(increased_happines)}. Employees are happy!")
# else:
#     print(f"Score: {len(increased_happines) - unhappy}/{len(increased_happines)}. Employees are not happy!")


happiness = [int(x) for x in input().split()]
factor = int(input())

increased_happiness = [z * factor for z in happiness]
average_happiness = sum(increased_happiness) / len(increased_happiness)

if len(increased_happiness) / 2 <= len([y for y in increased_happiness if y > average_happiness]):
    print(
        f"Score: {len([y for y in increased_happiness if y > average_happiness])}/{len(increased_happiness)}. Employees are happy!")
else:
    print(
        f"Score: {len([y for y in increased_happiness if y > average_happiness])}/{len(increased_happiness)}. Employees are not happy!")
