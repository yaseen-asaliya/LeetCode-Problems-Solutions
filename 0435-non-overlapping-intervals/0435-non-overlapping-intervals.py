class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        to_remove = 0

        intervals.sort(key=lambda x: x[0])

        prev = 0
        for curr in range(1, len(intervals)):
            if intervals[prev][1] > intervals[curr][0]:
                to_remove += 1

                if intervals[prev][1] > intervals[curr][1]:
                    prev = curr 
            else:
                prev = curr  
                
        return to_remove