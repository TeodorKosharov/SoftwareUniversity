def grades(value):
    if 2 <= value <= 2.99:
        return 'Fail'
    elif 3 <= value <= 3.49:
        return 'Poor'
    elif 3.50 <= value <= 4.49:
        return 'Good'
    elif 4.50 <= value <= 5.49:
        return 'Very good'
    elif 5.50 <= value <= 6:
        return 'Excellent'


result = grades(value=float(input()))
print(result)
