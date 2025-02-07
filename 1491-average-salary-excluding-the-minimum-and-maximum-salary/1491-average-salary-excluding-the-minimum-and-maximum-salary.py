class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        if n == 1:
            return salary[0]

        min_val = salary[0]
        max_val = salary[1]
        total = 0

        for s in salary:
            if s < min_val:
                min_val = s
            elif s > max_val:
                max_val = s
            total += s

        return  (total - (min_val + max_val)) / (n - 2) 