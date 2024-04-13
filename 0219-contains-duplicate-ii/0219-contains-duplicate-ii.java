class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
      Map<Integer, Integer> numIndexMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (numIndexMap.containsKey(num)) {
                if (i - numIndexMap.get(num) <= k) {
                    return true;
                }
            }
            numIndexMap.put(num, i);
        }
        
        return false;
    }
}