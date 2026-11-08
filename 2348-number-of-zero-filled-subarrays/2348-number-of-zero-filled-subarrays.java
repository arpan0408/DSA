class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long zeros = 0, j = 0;

        for(int i=0; i<nums.length; i++){
            if(nums[i] == 0){
                j++;
            }else {
                zeros += j * (j + 1) / 2;
                j = 0;
            } 
        }
        return zeros + j * (j + 1) / 2;
    }
}