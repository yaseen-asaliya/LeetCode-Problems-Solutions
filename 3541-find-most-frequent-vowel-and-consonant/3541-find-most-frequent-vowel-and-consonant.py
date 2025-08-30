class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = (set(['a', 'e', 'i', 'o', 'u']))
        vowel_freq = {}
        not_vowel_freq = {}
        max_vowel_freq = 0
        max_not_vowel_freq = 0

        for x in s:
            if x in vowel:
                vowel_freq[x] = vowel_freq.get(x, 0) + 1
                if vowel_freq[x] > max_vowel_freq:
                    max_vowel_freq = vowel_freq[x]
            else:
                not_vowel_freq[x] = not_vowel_freq.get(x, 0) + 1
                if not_vowel_freq[x] > max_not_vowel_freq:
                    max_not_vowel_freq = not_vowel_freq[x]

        return max_vowel_freq + max_not_vowel_freq
