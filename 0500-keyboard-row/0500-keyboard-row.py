class Solution(object):
    def findWords(self, words):
        first_row, second_row, third_row = set("qwertyuiop"), set("asdfghjkl") ,set("zxcvbnm")
        first_row_len, second_row_len, third_row_len = len(first_row), len(second_row), len(third_row)
        result = []

        for word in words:
            word_set = set(word.lower()) 
            if len(word_set | first_row) == first_row_len or \
                len(word_set | second_row) == second_row_len or \
                len(word_set | third_row) == third_row_len:
                result.append(word)

        return result 