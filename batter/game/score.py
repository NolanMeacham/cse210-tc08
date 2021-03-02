from game.actor import Actor
from game.point import Point

class Score(Actor):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0 
        self.set_text(f'Score: {self.score}')
        position = Point(0,0)
        self.set_position(position)
        velocity = Point(0,0)
        self.set_velocity(velocity)
    
    def set_score(self, score):
        self.score += score

    def get_text_score(self):
        score = self.score
        self.set_text(f'Score :{score}')
        text = self.get_text()
        return text

    def get_score(self):
        return self.score