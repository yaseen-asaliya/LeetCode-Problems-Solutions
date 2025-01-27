class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""

        for s1, s2 in zip_longest(word1, word2):
            if s1:
                str1 += s1
            if s2:
                str2 += s2

        return str1 == str2
        