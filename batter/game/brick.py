from game.actor import Actor
from game.point import Point

class Brick(Actor):
    """Brick "is an" Actor
    This inherits the attributes of methods of the Actor class.
    Brick is a game piece that is destroyed when hit by the ball.

    Stereotype:
        Information Holder

    Attributes:
        points (int): the point value for a brick object

    
    All other attributes are inherited by the actor class, which holds
    the getters and setters for each.
    """
    def __init__(self, x, y):
        """
        Class constructor

        Args:
            self (Brick): an instance of Brick
            x (int): a value corresponding to the x position
            y (int): a value corresponding to the y position
        """
        position = Point(x, y)
        self.set_text("*")
        self.set_position(position)
        self._points = 0

    def get_points(self):
        """
        Args:
            self (Brick): an instance of Brick

        Returns:
            points(int): the point value for the brick object
        """
        return self._points

    def set_points(self, points):
        """
        Args:
            self (Brick): an instance of Brick
            points (int): the point value for the brick object
        """
        self._points = points


# # test the class
# brick1 = Brick(20, 5)
# print(brick1.get_text())