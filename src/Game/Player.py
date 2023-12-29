class Player:
    def __init__(self, name, card_deck, missions_deck, board, game_params):
        self.name = name
        self.player_deck = [card_deck.take_card_from_deck() for _ in range(5)]
        self.player_wagons = game_params["nb_wagons_per_player"]
