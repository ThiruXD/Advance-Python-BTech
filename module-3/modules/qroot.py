import cmath
import math

def calc_square_roots(num1):
    root_txt = ""

    # 1. Standard float square root
    root1 = math.sqrt(num1)
    root_txt += f"Standard math.sqrt({num1}) = {root1}\n"

    # 2. Using the exponent operator
    num2 = 49
    root2 = num2**0.5
    root_txt += f"Exponent operator ({num2} ** 0.5) = {root2}\n"

    # 3. Integer square root (rounded down)
    num3 = 30
    root3 = math.isqrt(num3)
    root_txt += f"Integer math.isqrt({num3}) = {root3}\n"

    # 4. Complex square root for negative numbers
    num4 = -16
    root4 = cmath.sqrt(num4)
    root_txt += f"Complex cmath.sqrt({num4}) = {root4}\n"

    return root_txt

