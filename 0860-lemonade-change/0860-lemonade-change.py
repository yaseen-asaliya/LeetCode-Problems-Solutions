class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        fives = 0
        tens = 0 

        for x in bills:
            if x == 5:
                fives += 1
            elif x == 10 and fives >= 1:
                tens +=1 
                fives -=1
            elif x == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
            else:
                return False
        
        return True

