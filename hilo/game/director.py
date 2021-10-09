from game.player import Player
from game.deck import Deck

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.deck = Deck()
        


    def start_game(self):
        print("\nYou start with a score of 300. You win 100 for a correct guess\nand lose 75 for an incorrect guess. Same card == 100 points. \nIn addition, this deck has 52 cards, and each is discarded after being the current card.\nGood luck!")
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """ """
        print(f"\nThe current card is {self.deck.current_card}")
        
        
        self.player.player_guess()
        

    def do_updates(self):
        points = self.player.get_points(self.player.higher_or_lower, self.deck.next_card, self.deck.current_card)
        self.score += points
        self.deck.draw_card()

    def do_outputs(self):
        """outputs score, current card value"""
        print(f"\nThe card that was pulled was a {self.deck.current_card}")
        print(f"Your score is: {self.score}")
        
        if self.player.can_draw(self.score) == True:
            choice = input("Do you want to draw again? [y/n] ")
            self.keep_playing = (choice.lower() == "y")
        else:
            print ("Thanks for playing!")
            self.keep_playing = False
