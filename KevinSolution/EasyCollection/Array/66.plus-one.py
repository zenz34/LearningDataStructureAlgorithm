class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOne2(digits)
    
    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        digits = [0] * (len(digits) + 1)
        digits[0] = 1
            
        return digits
    
    def plusOne1(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] > 0:
                break

        if digits[0] == 0:
            digits.insert(0, 1)
            
        return digits

    def plusOne0(self, digits: List[int]) -> List[int]:
        str_digits = map(str, digits)
        number_str = ''.join(str_digits)
        number = int(number_str)
        number += 1
        number_str = str(number)
        # not necessary since `str` is iterable, but just mirroring above.
        str_digits = iter(number_str)
        digits = map(int, str_digits)
        return list(digits)
