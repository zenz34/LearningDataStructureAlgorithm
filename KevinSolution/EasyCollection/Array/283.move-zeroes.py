class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Complexity comparison of LeetCode solution 2 vs 3:
        https://gist.github.com/dosentmatter/7dd5b3612eb5243f78fe57cbb59e2c15
        """
        return self.moveZeroes0(nums)
                
    def moveZeroes0(self, nums: List[int]) -> None:
        """
        Same as LeetCode solution 3.
        Loop and bring non-zeros down to slow pointer, `non_zero_end`.
        """

        non_zero_end = 0
        for i, num in enumerate(nums):
            if num != 0:
                # Swap instead of remove/append because remove is O(n)
                # and append might double internal array size
                # O(n) remove * O(n) loop would make it O(n**2)
                # 
                # Replace instead of swap because swapping does extra operations
                # when moving a zero to a location that might get replaced later?
                # No because by not keeping track of which elements have been already
                # zeroed, it will always take 2n operations
                # ie. n iterations, k (non-zero) moves, n - k zeroing
                if non_zero_end != i:
                    nums[non_zero_end], nums[i] = nums[i], nums[non_zero_end]
                non_zero_end += 1
