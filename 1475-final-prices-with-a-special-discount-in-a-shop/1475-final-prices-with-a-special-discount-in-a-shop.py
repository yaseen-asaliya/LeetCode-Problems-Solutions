class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]         
        stack = []                 

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                j = stack.pop()
                answer[j] = prices[j] - p
            stack.append(i)

        return answer