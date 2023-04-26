#!/usr/bin/python3
"""
You have 'n' number of locked boxes in front of you.
Each box is numbered sequentially from '0' to 'n - 1'
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.
    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for el in boxes[n]:
            if el not in unlocked and el < len(boxes):
                unlocked.append(el)
    if len(unlocked) == len(boxes):
        return True
    return False
