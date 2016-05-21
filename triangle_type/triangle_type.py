# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle


def triangle_type(a, b, c):
    sides = [a, b, c]
    hypotenuse = max(sides)
    sides.pop(sides.index(hypotenuse))

    if hypotenuse >= sum(sides):
        return 0
    else:
        lesser_squares = sum([
            side**2
            for side in sides
        ])
        if lesser_squares > hypotenuse**2:
            return 1
        if lesser_squares == hypotenuse**2:
            return 2
        if lesser_squares < hypotenuse**2:
            return 3
