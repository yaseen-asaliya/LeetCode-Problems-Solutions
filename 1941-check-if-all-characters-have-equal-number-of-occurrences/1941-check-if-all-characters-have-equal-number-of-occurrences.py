class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 1) + 1

        _, value = next(iter(freq.items()))

        for _, v in freq.items():
            if v != value:
                return False
        return True 

