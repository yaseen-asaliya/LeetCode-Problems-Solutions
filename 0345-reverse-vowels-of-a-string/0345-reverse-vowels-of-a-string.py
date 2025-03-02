class Solution:
    def isVowel(self, letter):
        if letter in ['a','A','e','E','i','I','o','O','u','U']:
            return True
        return False

    def reverseVowels(self, s: str) -> str:
        indexes = []
        n = len(s)
        s = list(s)

        p1 = 0
        p2 = n - 1
        while (p1 < p2):
            if self.isVowel(s[p1]) and self.isVowel(s[p2]):
                s[p1], s[p2] = s[p2], s[p1]
                p1+=1
                p2-=1
                continue

            if self.isVowel(s[p1]) and not self.isVowel(s[p2]):
                p2-=1
                continue
            
            if not self.isVowel(s[p1]) and self.isVowel(s[p2]):
                p1+=1
                continue
            
            p1+=1
            p2-=1
        
        return ''.join(s)

