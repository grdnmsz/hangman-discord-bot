class Player:
    def __init__(self, name: str, id: int):
        self.name, self.id = name, id


class HangmanGame:
    def __init__(self, players: dict):
        self.players = {player: 0 for player in players}
        self.game_on = False
        return

    def _help() -> str:
        return
        """Lancer une partie : !play .\n
            Commencer la partie : !start .\n
            Consulter les scores : !scores .\n
            Pour rejoindre une partie, dire moi ou approchant.\n
            Pour donner le mot que vous pensez être la réponse : \" mon_mot ! \" 
        """

    def check_win(self) -> bool:
        return

    def game_done(self):
        """ Saving results into db."""
