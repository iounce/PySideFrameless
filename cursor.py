# -*- coding: utf-8 -*-

import enum

# define cursor direction
class CursorDirection(enum.Enum):
    Default = -1
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    LeftTop = 4
    LeftBottom = 5
    RightBottom = 6
    RightTop = 7