# imports

class Player():
    """
    Code template for a person playing this HiLo card game

    Attributes:
    points (int): player's points. may also be kept in Director class if needed

    Methods:
    get_points()
    can_draw()
    """

    def __init__(self):
        """
        Initializes and sets attributes
        """
        self.points = 300
        self.higher_or_lower = ""
        """We need to have self attrubutes for drawn card and previous card.. possibly"""

    # def draw_card(self):
    #     """
    #     Draws a card from the Deck.
    #     """
    #     pass

    def get_points(self, guess, drawn_card, prev_card):
        """
        Calculates points subtracted or added based on success or failure to guess card.
        params:
            guess (str): must be either "higher" or "lower", based on user input
            drawn_card (int): the card that was drawn from the deck after the guess.
            prev_card (int): the card value that was drawn previously and guessed upon by the user.

        return: (int) number of points, positive if added, negative if subtracted.
        Will also update player.points because we don't know where we're storing that yet
        """
        points_owed = 0

        if guess.lower() == "higher":
            if drawn_card >= prev_card:
                points_owed = 100
            else:
                points_owed = -75

        elif guess.lower() == "lower":
            if drawn_card <= prev_card:
                points_owed = 100
            else:
                points_owed = -75

        return points_owed


    def can_draw(self):
        """
        Determines ability to keep playing.
        CURRENTLY BASED OFF OF player.points !! Please alert me to change it if necessary

        return: bool
        """
        if self.points <= 0:
            return False
        else:
            return True

    def player_guess(self):
        valid = False
        print("Do you think the next card is going to be higher or lower than the current card?")
        while not valid:
            user_hilo = input("Please input higher or lower: ")
            if user_hilo.lower() == 'higher' or user_hilo.lower() == 'lower':
                valid = True
            else:
                print('Please guess either higher or lower. Ties are a win.\n')
        self.higher_or_lower = user_hilo.lower()
        
