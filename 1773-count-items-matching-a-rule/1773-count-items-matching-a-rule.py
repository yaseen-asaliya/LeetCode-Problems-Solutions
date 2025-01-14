class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        index = 0
        count = 0

        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2

        for item in items:
            if item[index] == ruleValue:
                count+=1
        return count 
        
            