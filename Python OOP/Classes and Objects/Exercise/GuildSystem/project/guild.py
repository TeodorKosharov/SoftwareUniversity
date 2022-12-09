from Exercise.GuildSystem.project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [x.name for x in self.players]:
            return f"Player {player_name} is not in the guild."

        for current_player in self.players:
            if current_player.name == player_name:
                current_player.guild = "Unaffiliated"
                self.players.remove(current_player)
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f'Guild: {self.name}' + '\n'
        for player in self.players:
            result += player.player_info()

        return result
