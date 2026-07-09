class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s_len = len(sentence)

        if sentence[0] != sentence[s_len-1]:
            return False
        
        for x in range(s_len):
            if sentence[x] == ' ' and sentence[x-1] != sentence[x+1]:
                return False

        return True


