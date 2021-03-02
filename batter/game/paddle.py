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
        y = int(constants.MAX_Y - 3)
        position = Point(x, y)
        self.set_text("===========")
        self.set_position(position)
        self.paddle_points = []

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

    def return_x_list(self):
        """
        The paddle is 8 characters wide. This method will create a list of 
        the x position for each piece of the paddle.

        Args:
            self (Paddle): an instance of Paddle.

        Returns:
            x_list (list): holds the x positions for each part of the paddle.
        """
        x = self.get_position().get_x()


        x_list = []

        for i in range(8):

            x += 1
            x_list.append(x)
        for i in range(8):
            x -= 1
            x_list.append(x)


        return x_list

