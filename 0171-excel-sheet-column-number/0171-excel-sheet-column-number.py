class Solution:
    def get_index(self, letter):
        return ord(letter) - ord('A') + 1

    def titleToNumber(self, columnTitle: str) -> int:
        str_len = len(columnTitle)
        res = 0
        power = 1

        for letter in columnTitle:
            res += self.get_index(letter) * pow(26, str_len - power)
            power+=1
        
        return res
