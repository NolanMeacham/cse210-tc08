from game.actor import Actor
from game.point import Point

class Brick(Actor):
    """

    Stereotype:
        Information Holder

    Attributes:

    
    All other attributes are inherited by the actor class, which holds
    the getters and setters for each.
    """
    def __init__(self, x, y):
        """
        """
        position = Point(x, y)
        self.set_text("*")
        self.set_position(position)

        # TODO: If we want, add an attribute _points, which will be the
        # points that each brick is worth. Then we can create getters/setters
        # accordingly. This will allow us to have some bricks that are worth
        # more points or have different text.


# # test the class
# brick1 = Brick(20, 5)
# print(brick1.get_text())