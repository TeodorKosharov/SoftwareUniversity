from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        created_food = Bread(name, price) if food_type == 'Bread' else Cake(name, price)
        if created_food.name in [x.name for x in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(created_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        created_drink = Tea(name, portion, brand) if drink_type == 'Tea' else Water(name, portion, brand)
        if created_drink.name in [x.name for x in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(created_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        created_table = InsideTable(table_number, capacity) if table_type == 'InsideTable' else OutsideTable(
            table_number, capacity)
        if created_table.table_number in [x.table_number for x in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(created_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.is_reserved = True
                table.capacity -= number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        chosen_table = [x for x in self.tables_repository if x.table_number == table_number]
        if not chosen_table:
            return f"Could not find table {table_number}"
        table = chosen_table[0]
        foods_not_in_menu = []

        for food in food_names:
            if food in [x.name for x in self.food_menu]:
                food_object = [x for x in self.food_menu if x.name == food][0]
                table.food_orders.append(food_object)
            else:
                foods_not_in_menu.append(food)

        result = f'Table {table_number} ordered:\n'
        for order in table.food_orders:
            result += repr(order) + '\n'

        result += f'{self.name} does not have in the menu:\n'
        for absent_food in foods_not_in_menu:
            result += absent_food + '\n'

        return result.strip()

    def order_drink(self, table_number: int, *drinks_names):
        chosen_table = [x for x in self.tables_repository if x.table_number == table_number]
        if not chosen_table:
            return f"Could not find table {table_number}"
        table = chosen_table[0]
        drinks_not_in_menu = []

        for drink in drinks_names:
            if drink in [x.name for x in self.drinks_menu]:
                drink_object = [x for x in self.drinks_menu if x.name == drink][0]
                table.drink_orders.append(drink_object)
            else:
                drinks_not_in_menu.append(drink)

        result = f'Table {table_number} ordered:\n'
        for order in table.drink_orders:
            result += repr(order) + '\n'

        result += f'{self.name} does not have in the menu:\n'
        for absent_drink in drinks_not_in_menu:
            result += absent_drink + '\n'

        return result.strip()

    def leave_table(self, table_number: int):
        found_table = [x for x in self.tables_repository if x.table_number == table_number][0]
        result = f"Table: {table_number}\n"
        result += f"Bill: {found_table.get_bill():.2f}"
        return result

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            res = table.free_table_info()
            if res is not None:
                result += table.free_table_info() + '\n'
        return result

    def get_total_income(self):
        total = 0
        for table in self.tables_repository:
            total += table.get_bill()
        return f'Total income: {total:.2f}lv'
