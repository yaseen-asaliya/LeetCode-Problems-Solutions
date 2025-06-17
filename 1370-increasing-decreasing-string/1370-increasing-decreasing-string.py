class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []
        total_chars = len(s)

        while len(result) < total_chars:
            for i in range(26):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

            for i in range(25, -1, -1):
                if freq[i] > 0:
                    result.append(chr(i + ord('a')))
                    freq[i] -= 1

        return ''.join(result)