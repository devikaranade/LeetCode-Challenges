class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 0;
        int right = n-1;
        int sq;

        for (int i=n-1; i>=0; i--){
            if (Math.abs(nums[right])>Math.abs(nums[left])){
                sq = nums[right];
                right--;
            }
            else {
                sq = nums[left];
                left++;
            }
            res[i]=sq*sq;
        }
        return res;

    }
}