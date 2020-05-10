from itertools import islice

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSum1(nums, target)
    
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Remember nums to indices reverse mapping and check for complement.
        O(n)
        """
        nums_to_indices = {}
        for i, element in enumerate(nums):
            complement = target - element
            if complement in nums_to_indices:
                return [i, nums_to_indices[complement]]
            nums_to_indices[element] = i
    
    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        """
        Search for all combination pairs.
        O(n**2)
        """
        for i, element_i in enumerate(nums):
            decumulator = target - element_i
            for j, element_j in enumerate(islice(nums, i + 1, None), i + 1):
                if decumulator - element_j == 0:
                    return [i, j]
