import re

given_string = input()

destination_pattern = r'(=|/)(?P<destination>[A-Z][A-Za-z]{2,})(\1)'

matches = re.finditer(destination_pattern, given_string)
total_matches = []
travel_points = 0

for match in matches:
    current_destionation = match.group('destination')
    total_matches.append(current_destionation)
    travel_points += len(current_destionation)

print(f"Destinations: {', '.join(total_matches)}")
print(f"Travel Points: {travel_points}")
