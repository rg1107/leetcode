class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int result = 0;
        int quo = 0;
        while (numBottles >= numExchange) {
            quo = numBottles/numExchange;
            result += numExchange*quo;
            numBottles = numBottles - quo*(numExchange - 1);
        }
        return result + numBottles;
    }
}