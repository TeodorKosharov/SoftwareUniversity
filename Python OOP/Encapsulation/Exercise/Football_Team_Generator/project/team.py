from Exercise.Football_Team_Generator.project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player.name in [x.name for x in self.__players]:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        if player_name not in [x.name for x in self.__players]:
            return f"Player {player_name} not found"

        for player in self.__players:
            if player.name == player_name:
                return self.__players.pop(self.__players.index(player))
