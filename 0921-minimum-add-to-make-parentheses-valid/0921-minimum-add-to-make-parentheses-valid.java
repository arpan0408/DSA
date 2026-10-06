class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> open = new Stack<>();
        int closed = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(')
                open.push('(');
            else if (open.size() > 0)
                open.pop();
            else
                closed++;
        }
        return open.size() + closed;
    }
}