class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        temp_friends = set(friends)
        res = []

        for x in order:
            if x in temp_friends:
                res.append(x)
        
        return res 