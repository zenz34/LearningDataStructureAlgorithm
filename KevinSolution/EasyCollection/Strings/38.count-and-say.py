from itertools import chain, islice

class Solution:
    def countAndSay(self, n: int) -> str:
        return self.countAndSay1(n)

    def countAndSay1(self, n: int) -> str:
        """
        Iterative solution.
        """

        count_and_say = '1'

        for _ in range(n - 1):
            count_and_say = type(self).compute_next_count_and_say1(count_and_say)

        return count_and_say
        
    @staticmethod
    def compute_next_count_and_say1(current_count_and_say: str) -> str:
        """
        Compare next and guard with index check.
        """

        next_count_and_say_list = []
        
        last_index = len(current_count_and_say) - 1

        count = 1
        for i in range(len(current_count_and_say)):
            if (
                i < last_index and
                current_count_and_say[i] == current_count_and_say[i + 1]
            ):
                count += 1
            else:
                next_count_and_say_list.append(str(count) + current_count_and_say[i])
                count = 1

        return ''.join(next_count_and_say_list)
        
    @staticmethod
    def compute_next_count_and_say0(current_count_and_say: str) -> str:
        """
        Compare previous and add `None` to chars.
        """

        next_count_and_say_list = []

        count = 1
        previous_char = current_count_and_say[0]
        for current_char in chain(
            islice(current_count_and_say, 1, None),
            (None,)
        ):
            if previous_char == current_char:
                count += 1
            else:
                next_count_and_say_list.append(str(count) + previous_char)
                count = 1

            previous_char = current_char

        return ''.join(next_count_and_say_list)

    def countAndSay0(self, n: int) -> str:
        """
        Recursive solution.
        """

        def count_and_say_helper(count_and_say: str, n: int) -> str:
            if not n:
                return count_and_say

            count_and_say = type(self).compute_next_count_and_say1(count_and_say)

            return count_and_say_helper(count_and_say, n - 1)

        return count_and_say_helper('1', n - 1)
