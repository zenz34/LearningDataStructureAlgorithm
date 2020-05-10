class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.firstUniqChar0(s)
    
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        elif len(s) == 1:
            return 0

        char_to_index_map = {}
        for i, char in enumerate(s):
            if char in char_to_index_map:
                char_to_index_map[char] = float('inf')
            else:
                char_to_index_map[char] = i

        min_index = min(char_to_index_map.values())
        if min_index == float('inf'):
            return -1
        return min_index
