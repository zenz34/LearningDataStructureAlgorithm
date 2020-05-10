class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicate0(nums)
    
    def containsDuplicate0(self, nums: List[int]) -> bool:
        seen_elements = set()
        for element in nums:
            if element in seen_elements:
                return True
            seen_elements.add(element)
        return False
