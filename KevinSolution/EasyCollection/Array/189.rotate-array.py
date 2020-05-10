from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        return self.rotate4(nums, k)

    def rotate4(self, nums: List[int], k: int) -> None:
        """
        LeetCode solution 3.
        """

        if len(nums) <= 1:
            return

        k %= len(nums)
        if k == 0:
            return
        
        i = 0
        num_elements_rotated = 0
        
        while num_elements_rotated < len(nums):
            j = i
            temp = nums[j]
            while True:
                j = (j + k) % len(nums)
                temp, nums[j] = nums[j], temp
                num_elements_rotated += 1
                if i == j:
                    break
            i += 1
    
    def rotate3(self, nums: List[int], k: int) -> None:
        """
        LeetCode solution 3 but modified to match `rotate0()`.
        Add some length checks in beginning.
        Rename `count` -> `num_elements_rotated`.
        Rename `start`/`current` -> `i` is slow pointer.
        Rename `next` -> `j` is fast pointer.
        No need for `prev`, just swap with `i`.
        No need for `temp`, just use python swap.
        """

        if len(nums) <= 1:
            return

        k %= len(nums)
        if k == 0:
            return
        
        i = 0
        num_elements_rotated = 0
        
        while num_elements_rotated < len(nums):
            j = i
            while True:
                j = (j + k) % len(nums)
                num_elements_rotated += 1
                if i == j:
                    break
                # When `i == j`, don't actually need to swap self with self.
                # Swap from previous iteration already put correct element at index `i`.
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        LeetCode solution 4.
        """
        if len(nums) <= 1:
            return

        k %= len(nums)
        if k == 0:
            return

        nums.reverse()
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))
        
    def reverse(self, nums: List[int], start: int, end: int):
        length = end - start
        last_index = end - 1
        for offset in range(0, length // 2):
            nums[start + offset], nums[last_index - offset] = (
                nums[last_index - offset], nums[start + offset]
            )
    
    def rotate1(self, nums: List[int], k: int) -> None:
        return self.rotate1_helper(nums, len(nums), k)
        
    def rotate1_helper(self, nums: List[int], length: int, k: int) -> None:
        """
        Notice that when rotating a list, two partitions of the list maintain the same order:
        Input: [1,2,3,4,5,6,7] and k = 3
        Output: [5,6,7,    1,2,3,4]
        rotate 1 steps to the right: [7,    1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,    1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,    1,2,3,4]

        The way this works is by noticing that after using `swap_shift_to_end()` to
        move `length - k` elements to their correct position, the left sublist of length `k`
        is in order but just rotated.
        
        For example, after running `swap_shift_to_end([1,2,3,4,5,6,7], 7, 3)`, we get
        [7,5,6,    1,2,3,4]
        `1,2,3,4` are in the correct order and positions.
        `7,5,6` are in order, but they just need to be rotated by `2` to be in the correct positions.
        We will always get a sublist like this that is in order but may need rotation.
        The reason is because how `swap_shift_to_end()` works. It swaps to the workspace in order,
        but just cycles through the indices as space runs out.
        We can then recursively call `rotate1_helper()`.
        We just need to generalize how to get the rotation value `2`.
        
        Notice that the workspace elements were previously `4,5,6`, then became
        rotated when swapping to `7,5,6`. This means that it is unrotated every `% 3`.
        The rotation is controlled by the number of swaps done by `swap_shift_to_end()`.
        
        The number of swaps is `length - k`.
        The number of swaps that over-rotated the workspace is `(length - k) % k`
        For example,
        7,5,6 is over-rotated by `(7 - 3) % 3 == 4 % 3 == 1`
        
        We can reverse this rotation by doing a negative rotation:
        `- ((length - k) % k)`
        To make it positive, we can add the divisor `k`:
        `k - (length - k) % k`
        We can also just ignore it since `swap_shift_to_end()` negative shifts.
        Simplify:
        ```
        - ((length - k) % k)
        - (length % k)
        ```
        """
        if length <= 1:
            return

        k %= length
        if k == 0:
            return

        self.swap_shift_to_end(nums, length, k)
        self.rotate1_helper(nums, k, -(length % k))
            
    def swap_shift_to_end(self, nums: List[int], length: int, k: int) -> None:
        """
        Keep `k` elements indices at the start of the list as a workspace to swap in
        `length - k` elements to their correct location at the end of the list.
        Cycle through the workspace list to preserve order.
        
        Example:
        Input: [1,2,3,4,5,6,7] and length = 7, k = 3
        Steps:
        1. [1,2,3,    4,5,6,7] # left indices will be the workspace and right will be shifted to
        2. [4,2,3,    1,5,6,7] # swap(1, 4)
        3. [4,5,3,    1,2,6,7] # swap(2, 5)
        4. [4,5,6,    1,2,3,7] # swap(3, 6)
        4. [7,5,6,    1,2,3,4] # cycle back around in the workspace to preserve order. swap(4, 7)
        Output: [7,5,6,    1,2,3,4]
        """
        if length <= 1:
            return

        k %= length
        if k == 0:
            return

        i = 0
        j = k
        for _ in range(length - k):
            nums[i], nums[j] = nums[j], nums[i]
            i = (i + 1) % k
            j += 1

    def rotate0(self, nums: List[int], k: int) -> None:
        """
        See Theorem 7.2 proof:
        https://www.eecs70.org/static/notes/n7.pdf
        
        From this we know that if the `gcd(len(nums), k) === 1`,
        then `0, k, 2*k, ..., (len(nums) - 1)*k` are distinct `% len(nums)`.
        
        If `gcd(len(nums), k) > 1`, stepping by `k` will not touch all elements.
        We need to increment the starting range `i` by `1` to reach the next set elements.
        The `gcd_nums_k` tells us how many sets of elements there are.
        Each element set will have `len(nums) // gcd_nums_k` elements.
        Note that `len(nums) // gcd_nums_k` is a whole number, since `gcd_nums_k` is a divisor
        of `len(nums)`.
        
        Proof of why GCD works:
        It has to do with a cycle repeating which is the LCM(len(nums), k).
        You can then calculate the number of elements in a cycle by doing:
        LCM / k since k is the hop length
        len(nums) / # elements in a cycle === # of cycles
        === len(nums)/ (LCM(len(nums), k) / k
        Then use formula in links 2 and 3 to change LCM to GCD.
        https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm
        https://www.chegg.com/homework-help/interesting-relationship-gcd-lcm-two-numbers-product-two-num-chapter-8.3-problem-40e-solution-9780536974105-exc
        https://proofwiki.org/wiki/Product_of_GCD_and_LCM
        
        If you need to calculate `gcd()` manually, can use Euclid's algorithm in n7.pdf.
        Can also use Extended Euclid's algorithm in n7.pdf.
        Implementation:
        https://www.geeksforgeeks.org/gcd-in-python/
        """

        gcd_nums_k = gcd(len(nums), k)
        # `- 1` because we are swapping, so the last swap puts two elements in their
        # correct location.
        num_swaps_per_element_set = len(nums) // gcd_nums_k - 1

        for i in range(gcd_nums_k):
            j = i
            for _ in range(num_swaps_per_element_set):
                j = (j + k) % len(nums)
                nums[i], nums[j] = nums[j], nums[i]
