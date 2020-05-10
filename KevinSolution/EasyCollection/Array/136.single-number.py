from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR all numbers. Duplicates will cancel each other out.
        """
        return reduce(lambda x, y: x ^ y, nums)
