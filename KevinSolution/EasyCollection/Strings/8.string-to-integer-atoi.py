INT_MIN = -2**31
INT_MAX = 2**31 - 1

class Solution:
    def myAtoi(self, str: str) -> int:
        return self.myAtoi0(str)
    
    def myAtoi0(self, str: str) -> int:
        accumulator = 0
        negate = 1
        num_begin = False
        for char in str:
            if char == ' ':
                if num_begin:
                    break
                continue
            elif not num_begin and char == '-':
                num_begin = True
                negate = -1
            elif not num_begin and char == '+':
                num_begin = True
                negate = 1
            elif char.isdecimal():
                num_begin = True
                accumulator *= 10
                accumulator += negate * int(char)
                if accumulator < INT_MIN:
                    return INT_MIN
                elif INT_MAX < accumulator:
                    return INT_MAX
            else:
                break
        return accumulator
