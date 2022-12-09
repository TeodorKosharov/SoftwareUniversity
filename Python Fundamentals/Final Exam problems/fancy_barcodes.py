import re

n = int(input())

barcode_pattern = r'(?P<a>@)#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z](?P=a)#{1,}'

for _ in range(n):
    barcode = input()
    match = re.search(barcode_pattern, barcode)
    if match:
        extracted_barcode = match.group()
        extracted_barcode = extracted_barcode.replace('@', '')
        extracted_barcode = extracted_barcode.replace('#', '')
        group_match = re.findall(r'\d+', extracted_barcode)
        if group_match:
            print(f"Product group: {''.join(group_match)}")
        else:
            print('Product group: 00')
    else:
        print("Invalid barcode")
