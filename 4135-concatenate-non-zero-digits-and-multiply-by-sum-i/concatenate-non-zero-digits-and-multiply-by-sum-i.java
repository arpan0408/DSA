class Solution {
    public long sumAndMultiply(int n) {
        long x = 0, sum = 0;

        while(n>0){
            if(n%10 != 0)
                x = (x*10) + n%10;
            n /= 10;
        }
        long tp = x;

        while(tp>0){
            sum += tp%10;
            tp /= 10;
        }

        tp = x;
        x = 0;
        while(tp > 0){
            x = (x*10) + (tp%10);
            tp /= 10;
        }
        return (x*sum);
    }
}