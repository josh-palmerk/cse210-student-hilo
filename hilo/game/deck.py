import random

class Deck:
    def __init__(self):
        self.deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
        self.next_card = random.randint(1, 13)
        self.current_card = random.randint(1, 13)
        self.num_cards = 0
    """We might need to add a self.current card or something like that so we can use it in the director"""
    """We also need a function that will change the new card to the current card. Not sure how you want to go about doing that"""
    def draw_card(self):
        self.current_card = self.next_card
        next_card_position = random.randint(0, 51)
        if self.deck[next_card_position]:
            self.next_card = self.deck[next_card_position]
            self.deck[next_card_position]=0
            self.num_cards += 1
        elif not self.deck[next_card_position]:
            self.draw_card()
        if self.num_cards == 52:
            print("Shuffling deck...")
            self.deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
            self.num_cards = 0
        return self.next_card


# class Deck:
#      def __init__(self):
#          self.deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
#          self.next_card = random.randint(1, 13)
#          self.current_card = random.randint(1, 13)
#          self.num_cards = 0    

#      def draw_card(self):
#         self.current_card = self.next_card
#         self.next_card = random.randint(1, 13)
