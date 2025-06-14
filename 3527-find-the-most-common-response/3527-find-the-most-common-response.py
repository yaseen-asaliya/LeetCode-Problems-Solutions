class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        temp_set = set()
        freq = {}
        
        for survey in responses:
            for response in survey:
                temp_set.add(response)
            
            for res in temp_set:
                if res in freq:
                    freq[res] += 1
                else:
                    freq[res] = 1

            temp_set.clear()

        freq = list(freq.items())
        n = len(freq)
        for i in range(n):
            for j in range(0, n - i - 1):
                if freq[j][1] < freq[j + 1][1]:
                    freq[j], freq[j + 1] = freq[j + 1], freq[j]

        res = []
        temp = freq[0][1]

        for item in freq:
            if item[1] == temp:
                res.append(item)
            else:
                break
                    
        n = len(res)
        for i in range(n):
            for j in range(0, n - i - 1):
                if res[j][0] > res[j + 1][0]: 
                    res[j], res[j + 1] = res[j + 1], res[j]

        return res[0][0]
