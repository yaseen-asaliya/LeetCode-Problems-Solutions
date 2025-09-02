class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            i = 0
            j = len(word)-1
            exists = True

            while i < j:
                if word[i] != word[j]:
                    exists = False
                    break
                i+=1
                j-=1
            if exists:
                return word

        return ""