class Solution(object):
    def maximumWealth(self, accounts):
        maxx = 0
        total = 0

        for customer in accounts:
            for bank in customer:
                total+= bank
            if total > maxx:
                maxx = total
            total = 0
        return maxx