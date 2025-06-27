class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq = {}
        res = []
        temp = []

        for person in range(len(groupSizes)):
            if not groupSizes[person] in freq:
                freq[groupSizes[person]] = [person]
            else:
                freq[groupSizes[person]].append(person)

        for group_size, values in freq.items():
            counter = 0
            
            for val in values:
                if counter != group_size:
                    temp.append(val)
                    counter+=1
                else:
                    res.append(temp)
                    counter = 1
                    temp = [val]

            if temp:
                res.append(temp)
                temp = []
        
        return res 