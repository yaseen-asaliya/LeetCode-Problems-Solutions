class Solution:
    def isCapital(self, letter):
        return letter > 'A' and letter < 'Z'

    def detectCapitalUse(self, word: str) -> bool:
        if self.isCapital(word[0]) and not self.isCapital(word[1]):
            if any(self.isCapital(x) for x in word[2:]):
                return False  
        elif not self.isCapital(word[0]):
            if any(self.isCapital(x) for x in word[1:]):
                return False  
        elif self.isCapital(word[0]) and self.isCapital(word[1]):
            if any(not self.isCapital(x) for x in word[3:]):
                return False  

        return True