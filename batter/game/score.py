from game.actor import Actor
from game.point import Point

class Score(Actor):
    """
    A class that will store the current score of the game. 
    Inherits the actor class. 
    """

    def __init__(self) -> None:
        super().__init__()
        self.score = 0 
        self.set_text(f'Score: {self.score}')
        position = Point(0,0)
        self.set_position(position)
        velocity = Point(0,0)
        self.set_velocity(velocity)
    """
    set_score:
    args:
        self: instance of a Score class
        score: the score earned will be added to the total score
    """
    def set_score(self, score):
        self.score += score
    """
    get_text_score:
    args:
        self: instance of a Score class

        grabs the score int and set's the actor text to a displayable text for game
    """
    def get_text_score(self):
        score = self.score
        self.set_text(f'Score :{score}')
        text = self.get_text()
        return text

    """
    returns the score
    args:
        self: instance of a Score class
    """
    def get_score(self):
        return self.score