class Solution(object):
    def firstUniqChar(self, s):
        dicts = {}

        for letter in s:
            if not letter in dicts:
                dicts[letter] = 1
            else:
                dicts[letter]+=1

        index = -1
        first = True
        
        for key, value in dicts.items():
            if value == 1 and first:
                index = s.index(key)
                first = False
            elif value == 1 and not first and s.index(key) < index:
                index = index = s.index(key)
        
        return index
