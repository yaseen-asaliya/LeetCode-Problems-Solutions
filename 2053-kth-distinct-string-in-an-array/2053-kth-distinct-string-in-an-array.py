class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp = {}
        indexes = []

        for letter in arr:
            temp[letter] = temp.get(letter, 0) + 1

        for key, val in temp.items():
            if val == 1:
                indexes.append(key)

        if len(indexes) < k:
            return ""
            
        return indexes[k-1]
        
        
