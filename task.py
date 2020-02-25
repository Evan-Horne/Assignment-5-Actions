import math
import datetime


def firstrun():
    return "success"


def circleArea(radius):
    return math.pi * (radius ** 2)


def firstAndLast(arr):
    return arr[0], arr[-1]


def numDays(d1, d2):
    return (d2 - d1).days
