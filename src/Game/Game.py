import random


class CardDeck:
    def __init__(self):
        self.colors = ["black", "orange", "pink", "red", "white", "yellow", "blue", "green"]
        self.special_color = "grey"
        self.deck = self.create_deck()
        self.discard_pile = []
        self.visible_cards = [self.take_card_from_deck() for _ in range(5)]
        self.check_grey_cards()

    def create_deck(self):
        deck = [color for color in self.colors for _ in range(12)] + [self.special_color for _ in range(14)]
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
            card_index = cards.index(color)
            card_choosen = cards.pop(card_index)
            self.refill_visible_cards()
            return card_choosen
        except ValueError:
            print(f"Aucune carte de couleur {color} trouvée.")
            return None

    def consume_cards(self, cards_list):
        self.discard_pile += cards_list

    def reveal_tunnel_cards(self):
        cards_revealed = [self.take_card_from_deck() for _ in range(3)]
        return cards_revealed

    def Action(self,color_choice, again):
        # Ajouter le fait qu'on doit checker les cartes visibles
        if not again:
            break
        else :
            if color_choice = 'grey':
                return self.take_visible_card('grey')
            elif color_choice = 'random':
                return self.take_card_from_deck(), self.Action(color_choice,true)
            else :
                cards_choosen = self.take_visible_card(color_choice), self.Action(color_choice,true)



deck = Deck()
deck.start_game()
