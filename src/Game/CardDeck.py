import random


class CardDeck:
    def __init__(self, game_params):
        self.colors = ["black", "orange", "pink", "red", "white", "yellow", "blue", "green"]
        self.special_color = "grey"
        self.deck = self.create_deck()
        self.discard_pile = []
        self.visible_cards = [self.take_card_from_deck() for _ in range(5)]
        self.check_grey_cards()
        self.nb_cards_per_color = game_params["nb_cards_per_color"]
        self.nb_grey_cards = game_params["nb_grey_cards"]

    def create_deck(self):
        deck = [color for color in self.colors for _ in range(self.nb_cards_per_color)] + [self.special_color for _ in range(self.nb_grey_cards)]
        random.shuffle(deck)
        return deck

    def refill_deck(self):
        self.deck = self.discard_pile
        random.shuffle(self.deck)
        self.discard_pile = []

    def display_visible_vard(self):
        return self.visible_cards

    def refill_visible_cards(self):
        if not self.deck:
            self.refill_deck()
        self.visible_cards.append(self.deck.pop())
        self.check_grey_cards()

    def take_card_from_deck(self):
        if not self.deck:
            self.refill_deck()
        card_choosen = self.deck.pop()
        return card_choosen

    def check_grey_cards(self):
        grey_count = self.visible_cards.count(self.special_color)
        while grey_count >= 3:
            self.discard_pile += self.visible_cards
            self.visible_cards = [self.take_card_from_deck() for _ in range(5)]

    def take_visible_card(self, color):
        try:
            card_index = self.visible_cards.index(color)
            card_choosen = self.visible_cards.pop(card_index)
            self.refill_visible_cards()
            return card_choosen
        except ValueError:
            print(f"Aucune carte de couleur {color} trouvée.")
            return None

    def consume_cards(self, cards_list):
        self.discard_pile += cards_list

    def reveal_tunnel_cards(self):
        cards_revealed = [self.take_card_from_deck() for _ in range(3)]
        self.discard_pile += cards_revealed
        return cards_revealed

    def action_get_cards(self, color_choice, again, cards_choosen):
        if not again or len(cards_choosen) == 2:
            return cards_choosen
        else:
            if color_choice == "grey":
                cards_choosen.append(self.take_visible_card("grey")), self.action_get_cards(color_choice, False, cards_choosen)
            elif color_choice == "random":
                cards_choosen.append(self.take_card_from_deck())
                return self.action_get_cards(color_choice, True, cards_choosen)
            else:
                cards_choosen.append(self.take_visible_card(color_choice))
                return self.action_get_cards(color_choice, True, cards_choosen)
