import random
from game import constants
from game.action import Action
from game import constants
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        balls = cast["balls"][0] # there's only one
        bricks = cast["bricks"]
        paddle = cast["paddle"][0]# there's only one
        for brick in bricks:
            if balls.get_position().equals(brick.get_position()) and brick.get_text() == "*"  :
                balls.set_velocity(balls.get_velocity().horizontal_collision())
                brick.set_text("")
            else:
                pass

        for x in paddle.return_x_list():
            if (balls._position._y == 17) and ((balls._position._x -5) < x < (balls._position._x +5)) :
                balls.set_velocity(balls.get_velocity().horizontal_collision())


            # if balls._position.get_y() == pad.get_y():
            #     balls.set_velocity(balls.get_velocity().horizontal_collision())

        if balls.get_position().get_y() == constants.MAX_Y - 1:
            quit()
        if balls.get_position().get_x() == constants.MAX_X - 1 or balls.get_position().get_x() == 1:
            balls.set_velocity(balls.get_velocity().vertical_collision())
        if balls.get_position().get_y() == 1:
            balls.set_velocity(balls.get_velocity().horizontal_collision())