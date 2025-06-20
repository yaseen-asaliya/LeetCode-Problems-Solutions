class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}   
        result = []    

        for ch in range(len(s)):
            last_index[s[ch]] = ch
        
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result