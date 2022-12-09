from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def change_need_sustenance(player):
        player.need_sustenance = player.stamina < 100

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player.name not in [x.name for x in self.players]:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [x.name for x in self.players]:
            return None
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return None
        if sustenance_type == 'Food' and sustenance_type not in [type(x).__name__ for x in self.supplies]:
            raise Exception("There are no food supplies left!")
        if sustenance_type == 'Drink' and sustenance_type not in [type(x).__name__ for x in self.supplies]:
            raise Exception("There are no drink supplies left!")

        chosen_player = [x for x in self.players if x.name == player_name][0]

        if not chosen_player.need_sustenance:
            return f"{player_name} have enough stamina."

        for index in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[index]).__name__ == sustenance_type:
                chosen_supply = self.supplies[index]
                self.supplies.remove(chosen_supply)
                break

        if chosen_player.stamina + chosen_supply.energy > 100:
            chosen_player.stamina = 100
        else:
            chosen_player.stamina += chosen_supply.energy

        Controller.change_need_sustenance(chosen_player)
        return f"{player_name} sustained successfully with {chosen_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [x for x in self.players if x.name == first_player_name][0]
        second_player = [x for x in self.players if x.name == second_player_name][0]

        if first_player.stamina <= 0 and second_player.stamina <= 0:
            result = f"Player {first_player_name} does not have enough stamina.\n"
            result += f"Player {second_player_name} does not have enough stamina."
            return result

        if first_player.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."

        attacking_player = first_player if first_player.stamina < second_player.stamina else second_player
        defending_player = first_player if attacking_player == second_player else second_player

        while True:
            try:
                defending_player.stamina -= (1 / 2) * attacking_player.stamina
            except ValueError:
                winner = attacking_player
                loser = defending_player
                defending_player.stamina = 0
                break

            attacking_player, defending_player = defending_player, attacking_player

        Controller.change_need_sustenance(loser)
        Controller.change_need_sustenance(winner)
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            for food in self.supplies:
                if type(food).__name__ == 'Food':
                    player.stamina += food.energy
                    self.supplies.remove(food)
                    break

            for drink in self.supplies:
                if type(drink).__name__ == 'Drink':
                    player.stamina += drink.energy
                    self.supplies.remove(drink)
                    break
            Controller.change_need_sustenance(player)

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'

        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()
