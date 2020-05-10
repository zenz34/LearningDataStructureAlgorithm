from operator import itemgetter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefix4(strs)

    def longestCommonPrefix4(self, strs: List[str]) -> str:
        """
        LeetCode solution 2 but do not slice if found min string that failed equality.
        """

        if not strs:
            return ""

        for i in range(len(strs[0])):
            str_index = type(self).find_str_index_char_i_not_equal(strs, i)
            if str_index:
                if i == len(strs[str_index]):
                    return strs[str_index]
                return strs[str_index][0:i]
        return strs[0]

    @staticmethod
    def find_str_index_char_i_not_equal(strs, i):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                return j
        return None

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        LeetCode solution 2.
        """

        if not strs:
            return ""

        for i in range(len(strs[0])):
            if not type(self).all_char_i_equal1(strs, i):
                return strs[0][0:i]
        return strs[0]

    @staticmethod
    def all_char_i_equal1(strs, i):
        for j in range(1, len(strs)):
            # Can also make caller return strs[j] if first operand of `or` is `True`
            # since it is shortest.
            # Only need to substring if second operand of `or` is `True`.
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                return False
        return True

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        Own solution. Compare each char at a time.
        Same as `longestCommonPrefix0()` but remember shortest string.
        """
        if not strs:
            return ""

        min_str_index, min_str_length = min(enumerate(map(len, strs)), key=itemgetter(1))

        for i in range(min_str_length):
            if not type(self).all_char_i_equal0(strs, i):
                return strs[min_str_index][0:i]
        return strs[min_str_index]

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        Own solution. Compare each char at a time.
        Same as `longestCommonPrefix0()` but while loop makes it easier in python,
        since `i` is not initialized by the for-loop if no iterations,
        and `i` is not incremented at the end of the for-loop.
        """
        if not strs:
            return ""

        min_str_length = min(map(len, strs))

        i = 0
        while i < min_str_length:
            if not type(self).all_char_i_equal0(strs, i):
                break
            i += 1
        return strs[0][0:i]

    def longestCommonPrefix0(self, strs: List[str]) -> str:
        """
        Own solution. Compare each char at a time.
        """
        if not strs:
            return ""

        min_str_length = min(map(len, strs))

        i = -1
        for i in range(min_str_length):
            if not type(self).all_char_i_equal0(strs, i):
                break
        else:
            i += 1
        return strs[0][0:i]

    @staticmethod
    def all_char_i_equal0(strs, i):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j - 1][i]:
                return False
        return True
