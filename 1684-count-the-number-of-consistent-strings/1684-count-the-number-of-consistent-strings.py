class Solution(object):
    def countConsistentStrings(self, allowed, words):
        num_of_consistance = 0
        consistance = True

        allowed = set(allowed)

        for word in words:
            for letter in word:
                if not letter in allowed:
                    onsistance = False
                    break
                onsistance = True

            if onsistance:
                num_of_consistance+=1
                
        return num_of_consistance
        