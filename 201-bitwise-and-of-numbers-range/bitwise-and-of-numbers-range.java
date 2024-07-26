class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        while(right>left)
           right = right & right-1;
        return left&right;
        // int pow = 0;
        // int result = 0;
        // int l = left;
        // int r = right;
        // while (left > 0 && right > 0) {
        //     int lbit = left&1;
        //     int rbit = right&1;

        //     if (lbit == 1 && rbit == 1 && r-l < Math.pow(2, pow)) {
        //         result += (int)Math.pow(2, pow);
        //     }
        //     pow++;
        //     left = left >> 1;
        //     right = right >> 1;
        // }

        // return result;
    }
}