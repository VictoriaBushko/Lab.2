import math

a = 0.1
b = 0.6
h = 0.05
d = 0.001

def calculate_series(x, d):
    k = 1
    sum_series = 0
    term = float('inf')
    while abs(term) > d:
        term = (k * x ** k)
        sum_series += term
        k += 1

    return sum_series

x = a

while x <= b:
    result = calculate_series(x, d)
    print(f"x = {x:.2f}, f(x) = {result:.6f}")

    x += h
    x = round(x, 2)
    print(x)