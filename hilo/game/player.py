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

        self.points += points_owed
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