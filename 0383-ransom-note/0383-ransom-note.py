class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in set(ransomNote):
            if char not in magazine or magazine.count(char) < ransomNote.count(char):
                return False
        
        return True