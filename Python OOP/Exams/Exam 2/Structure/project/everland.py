from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f'Monthly consumption: {total:.2f}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            if room.expenses + room.room_cost > room.budget:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)
            else:
                room.budget -= room.room_cost + room.expenses
                result.append(
                    f'{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left.')
        return '\n'.join(result)

    def status(self):
        result = f'Total population: {sum([x.members_count for x in self.rooms])}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$'
            if room.children:
                for n, child in enumerate(room.children):
                    result += f'--- Child {n} monthly cost: {child.cost * 30:.2f}$'
            if hasattr(room, 'appliances'):
                appliance_expenses = sum([x.get_monthly_expense() for x in room.appliances])
                result += f'--- Appliances monthly cost: {appliance_expenses:.2f}$'

        return result
