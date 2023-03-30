#!/usr/bin/python3
""" Lockbox problem algorithm """


def canUnlockAll(boxes):
    keys = [0]

    for i in keys:
        for key in boxes[i]:
            if key < len(boxes) and key not in keys:
                keys.append(key)

    box_list = [j for box in boxes for j in box]

    if set(box_list).issubset(set(keys)):
        return True

    return False
