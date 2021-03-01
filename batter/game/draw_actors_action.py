from game.action import Action

class DrawActorsAction(Action):
    """

    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService

    """
    def __init__(self, output_service):
        """
        Class constructor.

        Args:
            output_service: an instance of Output_Service class.

        """
        self._output_service = output_service

    def execute(self, cast):
        """
        Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()

    
