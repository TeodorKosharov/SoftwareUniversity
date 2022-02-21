# string = input().split()
#
# full_str = ''.join(string)  # Правим цял стринг от елементите
#
# list_of_values = list(map(int, full_str))   # Създаваме лист от тези елементи чрез функцията list и заедно с нея -
#                                             # използваме и функцията map, за да преобразуваме елементите в целочислен тип
# list_of_values.sort(reverse=True)
#
# final_num = ''
#
# for element in list_of_values:
#
#     final_num += str(element)
#
# print(final_num)

numbers = input().split()

numbers.sort(reverse=True)

print(''.join(numbers))
