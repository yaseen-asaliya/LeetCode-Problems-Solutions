class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        magazine = list(magazine)
        
        for letter in ransomNote:
            if letter != '0': 
                z = magazine.index(letter) if letter in magazine else -1
                
                if z == -1:
                    return False
                
                magazine[z] = '0' 
                
        return True
