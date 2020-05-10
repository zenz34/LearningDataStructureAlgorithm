from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram0(s, t)

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
