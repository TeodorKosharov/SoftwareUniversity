def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for cheese, quantities in sorted_cheeses:
        result += cheese + "\n"
        quantities.sort(reverse=True)
        result += "\n".join([str(x) for x in quantities])
        result += "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
