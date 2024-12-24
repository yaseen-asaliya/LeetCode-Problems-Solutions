class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        word_count = {}
        for word in re.sub(r'[^a-zA-Z\s]', '', paragraph).lower().split():
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1

        max_freq = max(word_count.values())
        max_freq_keys = [key for key, value in word_count.items() if value == max_freq]
        return max_freq_keys[0]
                

                
        