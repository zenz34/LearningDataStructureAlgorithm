class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseString1(s)

    def reverseString1(self, s: List[str]) -> None:
        end = len(s)
        last_index = len(s) - 1
        for offset in range(len(s) // 2):
            s[offset], s[last_index - offset] =  s[last_index - offset], s[offset]

    def reverseString0(self, s: List[str]) -> None:
        s.reverse()
