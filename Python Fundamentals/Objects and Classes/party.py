class Party:
    def __init__(self):
        self.ppl = []

    def print_info(self):
        people_result = ', '.join(self.ppl)
        print(f'Going: {people_result}')
        print(f"Total: {len(self.ppl)}")


party = Party()
while True:

    current_ppl = input()

    if current_ppl == 'End':
        break

    party.ppl.append(current_ppl)

party.print_info()
