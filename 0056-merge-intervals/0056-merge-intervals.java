class Solution {
    public int[][] merge(int[][] intervals) {
        int len = intervals.length;
        if (len <= 1) {
            return intervals; 
        }
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        int[][] res = new int[len][];
        int index = 0;

        for (int i = 0; i < len; i++) {
            if (i == len - 1 || intervals[i][1] < intervals[i + 1][0]) {
                res[index++] = intervals[i];
            } else {
                int mergedEnd = Math.max(intervals[i][1], intervals[i + 1][1]);
                intervals[i + 1][0] = intervals[i][0]; 
                intervals[i + 1][1] = mergedEnd; 
            }
        }

        int[][] merged = new int[index][];
        System.arraycopy(res, 0, merged, 0, index);
        
        return merged;
    }
}
