# math already imported, default degrees and radians methods disabled


def degrees(rad):
    deg = rad * (180 / math.pi)
    if deg % 1 == 0:
        return str(int(deg)) + "deg"
    return "{0:.2f}".format(round(deg, 2)).rstrip("0") + "deg"


def radians(deg):
    rad = deg * (math.pi / 180)
    if rad % 1 == 0:
        return str(int(rad)) + "rad"
    return "{0:.2f}".format(round(rad, 2)).rstrip("0") + "rad"

math.degrees = degrees
math.radians = radians
