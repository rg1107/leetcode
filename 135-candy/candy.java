class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int result = 0;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);

        for (int i=0;i<n;i++) {
            if (i!= n-1 && ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]) {
                candies[i] = candies[i+1] + 1;
            }
            if (i > 0 && ratings[i] > ratings[i-1] && candies[i] <= candies[i-1]) {
                candies[i] = candies[i-1] + 1;
            }
        }

        for (int i=n-1;i>=0;i--) {
            if (i!= n-1 && ratings[i] > ratings[i+1] && candies[i] <= candies[i+1]) {
                candies[i] = candies[i+1] + 1;
            }
            if (i > 0 && ratings[i] > ratings[i-1] && candies[i] <= candies[i-1]) {
                candies[i] = candies[i-1] + 1;
            }
        }

        for (int i=0;i<n;i++) {
            System.out.print(candies[i] + " ");
            result += candies[i];
        }

        return result;
    }
}