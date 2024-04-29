class Solution {
    public void rotate(int[] nums, int k) {
        int vectorSize = nums.length;
        k = k % vectorSize;
        
        int[] tempArr = new int[k];
        int index = 0;

        for(int i = vectorSize - k; i < vectorSize; i++){
            tempArr[index++] = nums[i];
        }

        for(int i = vectorSize - 1; i >= k; i--){
            nums[i] = nums[i - k];
        }

        for(int i = 0; i < k; i++){
            nums[i] = tempArr[i];
        }
    }
}
