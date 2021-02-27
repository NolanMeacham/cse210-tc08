from game.actor import Actor
from game.point import Point
from game import constants

class Paddle(Actor):
    """
    Paddle "is an" Actor.
    This inherits the attributes and methods from the Actor class.
    Paddle is a game piece that is moved by the user. It is meant to 
    bounce the ball back into the game.

    Stereotype:
        Information Holder

    """
    def __init__(self):
        """
        Class constructor.

        Args:
            self (Paddle): an instance of Paddle.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        position = Point(x, y)
        self.set_text("===========")
        self.set_position(position)

    def move_left(self):
        """
        Changes the paddle's x position to the left by 3 units.

        Args:
            self (Paddle): an instance of Paddle.
        """
        new_x = self.get_position().get_x() - 3
        new_y = self.get_position().get_y()
        self.set_position(Point(new_x, new_y))

    def move_right(self):
        """
        Changes the paddle's x position to the right by 3 units.

        Args:
            self (Paddle): an instance of Paddle.
        """
        new_x = self.get_position().get_x() + 3
        new_y = self.get_position().get_y()
        self.set_position(Point(new_x, new_y))