from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Other person's answers:
        https://medium.com/@lenchen/leetcode-350-intersection-of-two-arrays-ii-1affad47cb15
        
        Python `.sort()` (Timsort) complexity:
        https://stackoverflow.com/a/25813800/7381355
        
        Followup:

        ---

        What if nums1's size is small compared to nums2's size? Which algorithm is better?

        I'm assuming both lists are still sorted. Because if `intersect1()` has to sort,
        the space complexity depends if sorting is done in-place. The time complexity of the sort
        will overshadow the time complexity of the `intersect1()` algorithm.
        So including sort, `intersect1()` time complexity could be:
        O(len(nums1)*log(len(nums1)) + len(nums2)*log(len(nums2))) time
        O(n) space
        
        If len(nums1) << len(nums2),
        `intersect1()`:
        O(len(nums2)) time
        O(1) space
        
        `intersect0()`:
        O(len(nums2)) time
        O(len(nums1)) space
        
        So `intersect1()` is better
        
        ---

        What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        `intersect1()` is fine because it doesn't read the whole list into memory at once.
        `intersect0()` is fine because it chooses the smaller list to read into memory and create a
        `Counter` from.
        """
        return self.intersect1(nums1, nums2)
    
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        If already sorted,
        O(len(nums1) + len(nums2)) time
        O(1) space
        """

        nums1.sort()
        nums2.sort()

        intersection = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            num1 = nums1[i]
            num2 = nums2[j]
            
            if num1 < num2:
                i += 1
            elif num2 < num1:
                j += 1
            else:
                intersection.append(num1)
                i += 1
                j += 1
        return intersection

    def intersect0(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        O(len(nums1) + len(nums2)) time
        O(min(len(nums1), len(nums2))) space
        """

        # make nums1 the smaller list so `nums1_counts` potentially uses less memory.
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1_counts = Counter(nums1)

        intersection = []
        for element in nums2:
            if nums1_counts[element]:
                intersection.append(element)
                nums1_counts[element] -= 1
        return intersection
