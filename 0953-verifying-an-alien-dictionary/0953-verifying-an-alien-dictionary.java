class Solution {
    public boolean isAlienSorted(String[] words, String order) {

        int[] rank = new int[26];

        for (int i = 0; i < order.length(); i++) {
            rank[order.charAt(i) - 'a'] = i;
        }

        for (int i = 0; i < words.length - 1; i++) {
            if (!inCorrectOrder(words[i], words[i + 1], rank)) {
                return false;
            }
        }

        return true;
    }

    private boolean inCorrectOrder(String a, String b, int[] rank) {

        int minLen = Math.min(a.length(), b.length());

        for (int i = 0; i < minLen; i++) {

            char ch1 = a.charAt(i);
            char ch2 = b.charAt(i);

            if (ch1 != ch2) {
                return rank[ch1 - 'a'] < rank[ch2 - 'a'];
            }
        }

        // Prefix case
        return a.length() <= b.length();
    }
}
