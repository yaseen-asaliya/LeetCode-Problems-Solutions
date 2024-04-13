class Solution {
    public long countBadPairs(int[] nums) {
        long count=0;
        HashMap<Integer,Integer> mp= new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int prev= mp.getOrDefault(i-nums[i],0);
            count+= i- prev;
            mp.put(i-nums[i],prev+1);
        }
        return count;
    }
}
