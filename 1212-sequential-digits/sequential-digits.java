class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> list = new ArrayList<>();
        String num = "123456789";
        
        for(int i=String.valueOf(low).length(); i<=String.valueOf(high).length(); i++){
            for(int j=0; j+i <= num.length(); j++){
                int n = Integer.parseInt(num.substring(j, j+i));
                if(n >= low && n <= high)
                    list.add(n);
            }
        }
        return list;
    }
}