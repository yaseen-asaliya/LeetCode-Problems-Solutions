class BinaryIndexTree {
    private int[] tree;

    public BinaryIndexTree(int n) {
        this.tree = new int[n + 1];
    }

    public void update(int index, int diff) {
        int tid = index + 1;
        for (; tid < tree.length; tid += (tid & -tid)) {
            tree[tid] += diff;
        }
    }

    public int getSum(int index) {
        int tid = index + 1;
        int sum = 0;
        for (; tid > 0; tid -= (tid & -tid)) {
            sum += tree[tid];
        }
        return sum;
    }
}

class Solution {
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        List<int[]> sorted = new ArrayList<>(n);

        for (int i = 0; i < n; i++)
            sorted.add(new int[]{nums[i], i});

        Collections.sort(sorted, (a, b) -> Integer.compare(a[0], b[0]));

        int[] count = new int[n];
        BinaryIndexTree bit = new BinaryIndexTree(n);
        for (int i = 0; i < n; i++) {
            int originalIndex = sorted.get(i)[1];
            count[originalIndex] = i - bit.getSum(originalIndex);
            bit.update(originalIndex, 1);
        }
        
        List<Integer> result = new ArrayList<>();
        for (int num : count) {
            result.add(num);
        }
        return result;
    }
}