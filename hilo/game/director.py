from game.player import Player
from game.deck import Deck

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.deck = Deck()
        


    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """ """
        print(f"The current card is {self.deck.next_card}")
        
        
        self.player.player_guess()
        self.deck.draw_card()

    def do_updates(self):
        points = self.player.get_points(self.player.higher_or_lower, self.deck.current_card, self.deck.next_card)
        self.score += points
        

    def do_outputs(self):
        """outputs score, current card value"""
        print(f"\nThe card that was pulled was a {self.deck.next_card}")
        print(f"Your score is: {self.score}")
        
        if self.player.can_draw():
            choice = input("Do you want to draw again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False