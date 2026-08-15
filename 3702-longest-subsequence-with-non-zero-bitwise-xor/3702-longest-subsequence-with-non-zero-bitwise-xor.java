class Solution {
    public int longestSubsequence(int[] nums) {
        int count = 0, xor = 0;
        int n = nums.length;
        for(int num : nums){
            xor ^= num;
            if(num == 0) count++;
        }
        if(xor != 0)
            return n;
        return count == n ? 0: n-1;
    }
}