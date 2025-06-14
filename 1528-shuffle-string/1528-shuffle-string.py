class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        my_list = [''] * len(indices)

        for index, ch in zip(indices, s):
            my_list[index] = ch
        
        return ''.join(my_list)

        