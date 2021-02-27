from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    """
    Ball "is an" Actor.
    This inherits the attributes and methos of the Actor class.
    Ball is a game piece that moves around and can bounce.
    
    Stereotype:
        Information Holder

    """
    def __init__(self):
        """
        Class constructor.
        Initializes the ball to the center of the screen with a velocity that
        is moving 1 unit to the right an 1 unit up.

        Args:
            self (Ball): an instance of Ball.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)
        self.set_text("@")
        self.set_position(position)
        self.set_velocity(velocity)


    def bounce_horizontal(self):
        """
        Bounces the ball horizontally, meaning that the x velocity is reversed
        and the y velocity remains the same.

        Args:
            self (Ball): an instance of Ball.
        """
        new_x = -1 * self.get_velocity().get_x()
        new_y = self.get_velocity().get_y()
        self.set_velocity(Point(new_x, new_y))

    def bounce_vertical(self):
        """
        Bounces the ball vertically, meaning that the y velocity is reversed
        and the x velocity remains the same.

        Args:
            self (Ball): an instance of Ball.
        """
        new_x = self.get_velocity().get_x() 
        new_y = -1 * self.get_velocity().get_y()
        self.set_velocity(Point(new_x, new_y))