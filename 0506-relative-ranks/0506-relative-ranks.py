class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score, reverse=True)
        static_data = ["Gold Medal","Silver Medal","Bronze Medal"]
        res = {}
        c = 4

        for athlete in temp:
            if len(static_data):
                res[athlete] = static_data.pop(0)
            else:
                res[athlete] = str(c)
                c+=1
        
        return [res[a] for a in score]



