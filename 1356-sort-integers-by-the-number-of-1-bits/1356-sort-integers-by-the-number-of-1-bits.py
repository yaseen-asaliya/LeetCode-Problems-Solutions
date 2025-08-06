class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        freq = {}

        for n in arr:
            c = bin(n).count('1') 
            if c not in freq:
                freq[c] = []
            freq[c].append(n)

        print(freq)

        result = []
        for key in sorted(freq.keys()):
            result.extend(sorted(freq[key]))
        return result