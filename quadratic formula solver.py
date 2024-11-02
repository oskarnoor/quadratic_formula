import math


# x = (-b +- sqrt(b*b - 4ac)/(2a)
def quadratic_formula_calc():
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    discriminant = b**2 - 4 * a * c
    print()
    if discriminant >= 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f"First solution:  {root1}")
        print(f"Second solution: {root2}")
        return
    print("Can't perform calculation, ")
    print("because can't take sqrt from negative number:")
    print(f"sqrt({discriminant})")


def main():
    quadratic_formula_calc()


if __name__ == "__main__":
    main()
