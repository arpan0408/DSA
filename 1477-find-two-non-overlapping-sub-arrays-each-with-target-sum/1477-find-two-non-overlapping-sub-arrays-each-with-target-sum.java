class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] best = new int[n];
        java.util.Arrays.fill(best, Integer.MAX_VALUE);

        int left = 0, sum = 0, minLen = Integer.MAX_VALUE;
        for (int right = 0; right < n; right++) {
            sum += arr[right];

            while (sum > target && left <= right) {
                sum -= arr[left++];
            }

            if (sum == target) {
                int len = right - left + 1;
                if (left > 0 && best[left - 1] != Integer.MAX_VALUE) {
                    minLen = Math.min(minLen, len + best[left - 1]);
                }
                minLen = Math.min(minLen, len);
            }

            best[right] = minLen;
        }

        // The above is not sufficient alone; we need prefix/suffix properly.
        // Correct approach below:
        java.util.Arrays.fill(best, Integer.MAX_VALUE);
        int ans = Integer.MAX_VALUE;

        // prefix minimum lengths of valid subarrays ending at or before i
        int[] prefix = new int[n];
        java.util.Arrays.fill(prefix, Integer.MAX_VALUE);

        left = 0;
        sum = 0;
        int shortest = Integer.MAX_VALUE;
        for (int right = 0; right < n; right++) {
            sum += arr[right];
            while (sum > target) {
                sum -= arr[left++];
            }
            if (sum == target) {
                shortest = Math.min(shortest, right - left + 1);
            }
            prefix[right] = shortest;
        }

        // scan from right, maintain shortest subarray starting at or after i
        int[] suffix = new int[n];
        java.util.Arrays.fill(suffix, Integer.MAX_VALUE);

        left = n - 1;
        sum = 0;
        shortest = Integer.MAX_VALUE;
        for (int right = n - 1; right >= 0; right--) {
            sum += arr[right];
            while (sum > target) {
                sum -= arr[left--];
            }
            if (sum == target) {
                shortest = Math.min(shortest, left - right + 1);
            }
            suffix[right] = shortest;
        }

        for (int i = 0; i + 1 < n; i++) {
            if (prefix[i] != Integer.MAX_VALUE && suffix[i + 1] != Integer.MAX_VALUE) {
                ans = Math.min(ans, prefix[i] + suffix[i + 1]);
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
