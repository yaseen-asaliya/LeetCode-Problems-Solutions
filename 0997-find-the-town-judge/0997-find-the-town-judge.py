class Solution(object):
    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return 1 
        
        trust_counts = {} 
        trusters = set()  
        
        for a, b in trust:
            trust_counts[b] = trust_counts.get(b, 0) + 1  
            trusters.add(a) 
        
        for person in range(1, n + 1):
            if trust_counts.get(person, 0) == n - 1 and person not in trusters:
                return person
        
        return -1 
