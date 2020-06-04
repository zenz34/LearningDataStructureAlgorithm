# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.firstBadVersion3(n)

    def firstBadVersion3(self, n):
        """
        LeetCode solution 2. Difference is that it keeps middle in search space
        when `isBadVersion(middle) == True`. Since the first potential bad
        version is preserved in range, a single version range is guaranteed to
        be true, so `while` loop doesn't need to handle `start == last` and knows
        `start` will be the first bad version.
        
        Also makes it easier to understand since start and last don't cross each other.
        """

        start = 1
        last = n

        while start < last:
            middle = start + (last - start) // 2
            if isBadVersion(middle):
                last = middle
            else:
                start = middle + 1

        return start

    def firstBadVersion2(self, n):
        """
        Iterative version of `firstBadVersion1`.
        """
        
        start = 1
        last = n

        while start <= last:
            middle_version = (start + last) // 2
            if isBadVersion(middle_version):
                last = middle_version - 1
            else:
                start = middle_version + 1
                
        return start

    def firstBadVersion1(self, n):
        """
        Recursive with base case check after call.
        """
        def firstBadVersion_helper(start, last):
            # When boundary is crossed and no versions in range, either:
            # 1. `start` is a bad version and the caller decremented last
            #    There is no version before `start` or the version before
            #    `start` is good.
            # 2. `start` was set to a good version until the caller incremented
            #    `start`. The incremented `start` has to be bad because it is
            #    the first version out of range. This means it was previously
            #    excluded for being a bad version.
            # In both cases, `start` is the first bad version.
            #
            # Another way to think about it is that `last < start` means a range
            # with 0 versions. Since the function was initially called on a version
            # range with a guaranteed bad version in it and the versions keeps halving,
            # hitting 0 versions means the next version must be the first bad one.
            #
            # It seems it's not always easiest to think of base case first since
            # this base case depends on the larger algorithm.
            if last < start:
                return start
            middle_version = (start + last) // 2
            if isBadVersion(middle_version):
                return firstBadVersion_helper(start, middle_version - 1)
            else:
                return firstBadVersion_helper(middle_version + 1, last)

        return firstBadVersion_helper(1, n)

    def firstBadVersion0(self, n):
        """
        Recursive with base case check before call.
        """
        def firstBadVersion_helper(start, last):
            middle_version = (start + last) // 2
            if isBadVersion(middle_version):
                if start == middle_version:
                    return start
                return firstBadVersion_helper(start, middle_version - 1)
            else:
                if middle_version == last:
                    return middle_version + 1
                return firstBadVersion_helper(middle_version + 1, last)

        return firstBadVersion_helper(1, n)
