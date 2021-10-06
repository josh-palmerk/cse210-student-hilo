from game.player import Player
from game.deck import Deck

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = 0
        self.player = player()
        self.deck = deck()


    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """ """
        self.deck.draw_card()

    def do_updates(self):
        points = self.player.get_points()
        self.score += points
        

    def do_outputs(self):
        """outputs score, current card value"""
        print(f"\nYou rolled: {self.thrower.dice}")
        print(f"Your score is: {self.score}")
        if self.deck.can_draw():
            choice = input("Do you want to continue? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False