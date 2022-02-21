from collections import deque


def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes = deque(args)

    while cubes:
        current_cube = cubes.popleft()
        if current_cube == 'Finish':
            return f"There is free space in the box. You could put {box_size} more cubes."
        if current_cube > box_size:
            cubes.appendleft(current_cube - box_size)
            return f'No more free space! You have {sum([x for x in cubes if type(x) == int])} more cubes.'
        box_size -= current_cube


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
