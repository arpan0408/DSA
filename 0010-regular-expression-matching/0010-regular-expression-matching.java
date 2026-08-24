class Solution {
    public boolean isMatch(String s, String p) {
        Boolean[][] bool = new Boolean[s.length() + 1][p.length()];
        return isMatch(s, p, 0, 0, bool);
    }

    private boolean isMatch(String s, String p, int sIdx, int pIdx, Boolean[][] bool){
        if(sIdx == s.length() && pIdx == p.length())
            return true;
        
        if(pIdx >= p.length()) return false;

        if(bool[sIdx][pIdx] != null) return bool[sIdx][pIdx];

        boolean charMatch = sIdx < s.length() && (s.charAt(sIdx) == p.charAt(pIdx) || p.charAt(pIdx) == '.');
        boolean nextonestar = pIdx + 1 < p.length() && p.charAt(pIdx + 1) == '*';
        
        final boolean isMatch;

        if(charMatch){
            if(nextonestar){
                isMatch = isMatch(s, p, sIdx, pIdx + 2, bool) || isMatch(s, p, sIdx + 1, pIdx, bool);
            } else{
                isMatch = isMatch(s, p, sIdx + 1, pIdx + 1, bool);
            }
        } else{
            if(nextonestar){
                isMatch = isMatch(s, p, sIdx, pIdx + 2, bool);
            } else{
                isMatch = false;
            }
        }
        bool[sIdx][pIdx] = isMatch;
        return isMatch;
    }
}