from math import log, cos, sin

a = 2
b = 4
h = 0.2

x = a

interval1 = 3
interval2 = 4.5
while x <= b:
    if x <= interval1:
        result = log(x ** 3)
    elif interval1 < x < interval2:
        result = x / abs(sin(x))
    else:
        result = 1 / cos(1 / x)

    print(f"x = {x:.2f}, f(x) = {result:.4f}")
    x += h
    x = round(x, 2)
    print(x)
