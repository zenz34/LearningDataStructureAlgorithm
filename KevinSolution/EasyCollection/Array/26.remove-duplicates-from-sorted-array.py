class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.removeDuplicates3(nums)
    
    def removeDuplicates3(self, nums: List[int]) -> int:
        """
        This algorithm is partially from leetcode solution. I have optimized it by
        ending early when seeing the `max_num = nums[-1]`.
        It is basically the same as what I have been doing below in other solutions.
        The difference is that it reverses the order that the pointers work.
        Previously, I advanced `i` until I saw an out-of-place element. Then I advanced
        `fringe_i` to find the correct element.
        This algorithm instead advances `fringe_i` until it sees the next correct element.
        Then it puts it where it belongs - the current `i` index.
        The benefit of this is that there is no need for nested loops.
        Time complexity is still the same O(n).
        """
        if len(nums) == 0:
            return 0

        i = 0
        fringe_i = 1
        while nums[i] < nums[-1]:
            if nums[i] < nums[fringe_i]:
                i += 1
                nums[i] = nums[fringe_i]
            fringe_i += 1
        return i + 1
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        Same as `removeDuplicates2()` but starts with `i = 0`. This increases all
        `nums[i + x]` access to `nums[i + 1 + x]` to cancel out the different initial value.
        """
        
        if len(nums) == 0:
            return 0

        i = 0
        fringe_i = 2
        while nums[i] < nums[-1]:
            if nums[i + 1] <= nums[i]:
                for fringe_i in range(fringe_i, len(nums)):
                    if nums[i] < nums[fringe_i]:
                        nums[i + 1] = nums[fringe_i]
                        break
            i += 1
            fringe_i += 1
        return i + 1
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        """
        Same algorithm as `removeDuplicates0()`, but don't keep track of `max_seen_num`
        and `max_num`. They are kept track in the array elements.
        `max_seen_num == nums[i - 1]`
        `max_num == nums[-1]`
        
        Not setting `max_seen_num = -float('inf')` anymore so have to increment both
        `i` and `fringe_i` by 1 to handle the initial case.
        """
        
        if len(nums) == 0:
            return 0

        i = 1
        fringe_i = 2
        while nums[i - 1] < nums[-1]:
            if nums[i] <= nums[i - 1]:
                for fringe_i in range(fringe_i, len(nums)):
                    if nums[i - 1] < nums[fringe_i]:
                        nums[i] = nums[fringe_i]
                        break
            i += 1
            fringe_i += 1
        return i

    def removeDuplicates0(self, nums: List[int]) -> int:
        """
        Loop through `nums`. If a number is <=, move `fringe_i` index to search for
        next increasing number.
        Can end early without looking at whole list since know the `max_num` of the list
        is `nums[-1]`.
        """

        if len(nums) == 0:
            return 0

        max_seen_num = -float('inf')
        max_num = nums[-1]

        i = 0
        fringe_i = 1
        while max_seen_num < max_num:
            if nums[i] <= max_seen_num: 
                for fringe_i in range(fringe_i, len(nums)):
                    if max_seen_num < nums[fringe_i]:
                        nums[i] = max_seen_num = nums[fringe_i]
                        break
            else:
                max_seen_num = nums[i]
            i += 1
            fringe_i += 1
        return i
