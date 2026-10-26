class Solution {
    public int findMin(int[] nums) {
        int min = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[min] > nums[i]) min = i;
        }
        return nums[min];
    }
}