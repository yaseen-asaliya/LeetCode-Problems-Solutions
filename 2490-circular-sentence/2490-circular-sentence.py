class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        for x in range(len(sentence)):
            if sentence[x] == ' ' and sentence[x-1] != sentence[x+1]:
                return False

        return True


