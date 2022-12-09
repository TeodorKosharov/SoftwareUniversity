def start_spring(**kwargs):
    flowers = {}
    result = ''

    for flower, flower_type in kwargs.items():
        if flower_type not in flowers:
            flowers[flower_type] = [flower]
            continue
        flowers[flower_type].append(flower)

    flowers = sorted(flowers.items(), key=lambda x: (-len(x[1]), x[0]))

    for current_flower, current_flower_types in flowers:
        result += f'{current_flower}:' + '\n'
        for current_flower_type in sorted(current_flower_types):
            result += f'-{current_flower_type}' + '\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }

print(start_spring(**example_objects))
