class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.isPalindrome1(s)

    def isPalindrome1(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].casefold() != s[j].casefold():
                return False
            else:
                i += 1
                j -= 1
        return True

    def isPalindrome0(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            while i <= j and not s[i].isalnum():
                i += 1
            while i <= j and not s[j].isalnum():
                j -= 1
            if i <= j and s[i].casefold() != s[j].casefold():
                return False
            i += 1
            j -= 1
        return True
