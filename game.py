class Player:
    def __init__(self, name: str, id: int):
        self.name, self.id = name, id


class HangmanGame:
    def __init__(self, players={}) -> None:
        self.players = {player: 0 for player in players}
        self.game_on = False
        self.secret_word = ''
        return

    def check_win(self) -> bool:
        return

    def game_done(self):
        """ Saving results into db."""

    def reset(self):
        self.players = {}
        self.game_on = False
        self.secret_word = ''
        return
