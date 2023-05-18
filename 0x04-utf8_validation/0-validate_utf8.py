#!/usr/bin/python3
"""UTF-8 Validation project"""


def validUTF8(data):
    """
    Validate if the data is in UTF-8 mode
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """

    b_cnt = 0

    for i in data:
        if b_cnt == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                b_cnt = 1
            elif i >> 4 == 0b1110:
                b_cnt = 2
            elif i >> 3 == 0b11110:
                b_cnt = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            b_cnt -= 1
    return b_cnt == 0
