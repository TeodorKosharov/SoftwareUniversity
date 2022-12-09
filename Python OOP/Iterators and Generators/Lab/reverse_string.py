def reverse_text(some_string):
    for char in some_string[::-1]:
        yield char


for char in reverse_text("step"):
    print(char, end='')

