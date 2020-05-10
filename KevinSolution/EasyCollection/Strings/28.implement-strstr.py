from itertools import islice, starmap, zip_longest
from operator import eq

map_longest = lambda function, *iterables: starmap(function, zip_longest(*iterables))

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStr8(haystack, needle)

    def strStr10(self, haystack: str, needle: str) -> int:
        """
        LeetCode solution 3.
        """
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31
        
        # lambda-function to convert character to integer
        h_to_int = lambda i : ord(haystack[i]) - ord('a')
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0
              
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1

    def strStr9(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison.
        Should be correct but too slow for LeetCode because no early exit.

        Same as `strStr4()` but uses pre-calculates for-loop length.
        """

        if needle == "":
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            # Don't need `map_longest` since did length check above.
            pairwise_char_equals = map(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                return i
        else:
            return -1

    def strStr8(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison. Should be correct but too slow for LeetCode.

        Same as `strStr3()` but uses pre-calculates for-loop length.
        """

        if needle == "":
            return 0

        index = -1

        for i in range(0, len(haystack) - len(needle) + 1):
            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            # Don't need `map_longest` since did length check above.
            pairwise_char_equals = map(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                index = i
                break

        return index

    def strStr7(self, haystack: str, needle: str) -> int:
        """
        LeetCode solution 1.
        """
        L, n = len(needle), len(haystack)

        # You can pre-calculate iteratiions as `n - L + 1` instead of doing length checks
        # like in `strStr5()` and `strStr6()`.
        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

    def strStr6(self, haystack: str, needle: str) -> int:
        """
        Use string slicing instead of iterative slicing.
        Should use more memory when strings are large.
        """

        if needle == "":
            return 0

        index = -1

        for i in range(len(haystack)):
            haystack_islice_max_length = len(haystack) - i
            if haystack_islice_max_length < len(needle):
                break

            found_needle = haystack[i: i + len(needle)] == needle
            if found_needle:
                index = i
                break

        return index

    def strStr5(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison.
        Should be correct but too slow for LeetCode because no early exit.

        Same as `strStr3()` but uses breaks early when `haystack` is too small.
        """

        if needle == "":
            return 0

        for i in range(len(haystack)):
            haystack_islice_max_length = len(haystack) - i
            if haystack_islice_max_length < len(needle):
                return -1

            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            # Don't need `map_longest` since did length check above.
            pairwise_char_equals = map(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                return i
        else:
            return -1

    def strStr4(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison. Should be correct but too slow for LeetCode.

        Same as `strStr2()` but uses breaks early when `haystack` is too small.
        """

        if needle == "":
            return 0

        index = -1

        for i in range(len(haystack)):
            haystack_islice_max_length = len(haystack) - i
            if haystack_islice_max_length < len(needle):
                break

            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            # Don't need `map_longest` since did length check above.
            pairwise_char_equals = map(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                index = i
                break

        return index

    def strStr3(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison.
        Should be correct but too slow for LeetCode because no early exit.

        Same as `strStr2()` but uses for-else.
        """

        if needle == "":
            return 0

        for i in range(len(haystack)):
            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            pairwise_char_equals = map_longest(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                return i
        else:
            return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        """
        Iterative string comparison.
        Should be correct but too slow for LeetCode because no early exit.
        """

        if needle == "":
            return 0

        index = -1

        for i in range(len(haystack)):
            # compare strings iteratively to avoid creating another string with slice.
            haystack_islice = islice(haystack, i, i + len(needle))
            pairwise_char_equals = map_longest(eq, haystack_islice, needle)
            found_needle = all(pairwise_char_equals)
            if found_needle:
                index = i
                break

        return index

    def strStr1(self, haystack: str, needle: str) -> int:
        """
        Cheating method
        """

        return haystack.find(needle)

    def strStr0(self, haystack: str, needle: str) -> int:
        """
        Cheating method
        """

        try:
            return haystack.index(needle)
        except ValueError:
            return -1

class RollingHash:
    """
    This is unfinished since decided not the best solution.
    """

    NUM_LOWERCASE_LETTERS = ord('z') - ord('a') + 1
    MODULUS = 2**31

    @staticmethod
    def letter_index(char):
        return ord(char) - ord('a')
    
    def __init__(self, string):
        # Maintaining just length won't work because need to remember string for sliding window.
        # Remembering a substring of `haystack` wastes memory.
        # Remembering `haystack` with indices works but is too much work and too specific to this
        # use case.
        # This rolling hash is better suited for other use cases. Complete it later.
        self.length = 0
        self.hash = 0

        for char in string:
            self.push(char)
        
    def push(self, char):
        self.length += 1

        self.hash *= type(self).NUM_LOWERCASE_LETTERS
        self.hash += type(self).letter_index(char)
        self.hash %= type(self).MODULUS
        
    def roll(self, char):
        # Have to handle case when length is 0.

        # Was gonna implement the non-generalized way
        # `(h_0 - 0 * 26**3) * 26`
        # since instead of the distributed
        # `(h_0 * 26 - 0 * 26**4)`
        # Since it has lower power so will "overflow" less.
        self.hash -= 0
        self.hash *= type(self).NUM_LOWERCASE_LETTERS
        self.hash += type(self).letter_index(char)
        self.hash %= type(self).MODULUS

    def __eq__(self, other):
        return (
            type(self) == type(other) and
            self.length == other.length and
            self.hash == other.hash
        )

    def __hash__(self):
        return hash((self.length, self.hash))
