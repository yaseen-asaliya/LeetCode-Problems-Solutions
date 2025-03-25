class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1, freq2 = [0] * 26, [0] * 26

        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for c in word2:
            freq2[ord(c) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0): 
                return False

        freq_count1, freq_count2 = {}, {}
        
        for f in freq1:
            if f > 0:
                freq_count1[f] = freq_count1.get(f, 0) + 1

        for f in freq2:
            if f > 0:
                freq_count2[f] = freq_count2.get(f, 0) + 1

        return freq_count1 == freq_count2