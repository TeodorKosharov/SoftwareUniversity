from math import floor
centuries = int(input())

years = centuries * 100
days = floor(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
