
from enum import Enum

class FacingDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    NONE = -1

class RobotModel:
    position = [-1,-1]
    facing = FacingDirection.NONE

    def __init__(self, position, facing):
        self.position = position
        self.facing = facing

    @classmethod
    def is_placed(cls):
        return len(cls.position) == 2 and cls.facing != FacingDirection.NONE

    @classmethod
    def report(cls):
        if not cls.position[0] == -1: return {"x": f"{cls.position[0]}", 'y': f"{cls.position[1]}", 'f': f"{cls.facing.name}" }
        else: return {}