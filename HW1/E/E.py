import random

def solution(x1, y1, x2, y2):
    if (x1, y1) != (x2, y2) and -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
        return True
    else:
        return False
