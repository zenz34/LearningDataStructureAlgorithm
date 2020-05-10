from math import fmod, trunc

class Solution:
    def reverse(self, x: int) -> int:
        return self.reverse1(x)

    def reverse1(self, x: int) -> int:
        reversed_x = 0

        while x != 0:
            # pop next digit
            # Can use `int` or `trunc`.
            # See:
            # https://stackoverflow.com/a/52224046/7381355
            least_significant_digit = int(fmod(x, 10))
            # Can't do `x //= 10` because `//` is floordiv not truncdiv.
            # Java int `/` is truncdiv.
            x = trunc(x / 10)

            reversed_x *= 10 # shift up a digit
            reversed_x += least_significant_digit # append next digit

            if reversed_x < -2**31 or 2**31 - 1 < reversed_x:
                return 0

        return reversed_x

    def reverse0(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        x = str(x)
        x = list(reversed(x))
        x = ''.join(x)
        x = int(x)
        
        reversed_x = sign * x
        if -2**31 <= reversed_x <= 2**31 - 1:
            return reversed_x
        return 0
