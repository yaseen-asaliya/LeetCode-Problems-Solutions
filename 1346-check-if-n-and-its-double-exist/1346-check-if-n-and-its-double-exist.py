class Solution(object):
    def checkIfExist(self, arr):
        arr.sort()
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * 2 == arr[j] or arr[i] == 2 * arr[j]:
                    return True
        return False