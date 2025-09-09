class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        remove = n // 20

        for _ in range(remove):
            min_val = arr[0]
            min_idx = 0
            for i in range(1, len(arr)):
                if arr[i] < min_val:
                    min_val = arr[i]
                    min_idx = i
            arr.pop(min_idx)

        for _ in range(remove):
            max_val = arr[0]
            max_idx = 0
            for i in range(1, len(arr)):
                if arr[i] > max_val:
                    max_val = arr[i]
                    max_idx = i
            arr.pop(max_idx)

        total = 0
        count = 0
        for v in arr:
            total += v
            count += 1

        return total / count