class Solution {
    public int maxDepth(String s) {
        int max = 0;
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '(') stack.push(c);
            if(c == ')'){
                max = Math.max(stack.size(), max);
                stack.pop();
            }
        }
        return max;
    }
}