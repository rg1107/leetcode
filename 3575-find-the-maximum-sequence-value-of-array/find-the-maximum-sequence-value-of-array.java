class Solution {
    /**
    https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/solutions/5794940/java-with-comments-in-code-find-all-possible-ors
     */
    public int maxValue(int[] nums, int k) {
        int n = nums.length;
        int ans = 0;
        /*
            find all possible OR at each index, from left and right,
            and store the count of elements that made that OR,
            We can do that because max OR we can have is 128
        */
        int[][][] lftOR = new int[n][128][2];
        int[][][] rgtOR = new int[n][128][2];
        /*
            [0] -> minimum count of nums needed to make that OR
            [1] -> maximum count of nums we can take to make that OR
        */
        lftOR[0][nums[0]][0] = lftOR[0][nums[0]][1] = 1;//first left element
        rgtOR[n-1][nums[n-1]][0] = rgtOR[n-1][nums[n-1]][1] = 1;//first right element

        // 'l'-> index for left array, 'r'-> index for right array
        for (int l=1, r=n-2; l < n-k; l++, r--) {
            /*
                we will iterate OR value in decreasing manner,
                because taking OR, may only increase num's value,
                so first we will copy count of OR, from previous index,
                and then update, if possible
            */
            for (int or=127; or > 0; or--) {
                // New-OR can only be made by taking OR with previous-ORs
                // Means min-count at previous index must be greater than zero
                if (lftOR[l-1][or][0] > 0) {
                    lftOR[l][or] = Arrays.copyOf(lftOR[l-1][or], 2);
                    /*
                        if min-count of nums needed to make curr-OR is less than K,
                        only then we can OR; current-num and current-OR
                    */
                    if (lftOR[l][or][0] < k) update(lftOR[l], or, or|nums[l]);
                }
                // Same we will do for right array
                if (rgtOR[r+1][or][0] > 0) {
                    rgtOR[r][or] = Arrays.copyOf(rgtOR[r+1][or], 2);

                    if (rgtOR[r][or][0] < k) update(rgtOR[r], or, or|nums[r]);
                }
            }
            // if current num taken alone
            update(lftOR[l], 0, nums[l]);
            update(rgtOR[r], 0, nums[r]);
        }

        // at each index, XOR all possible combinations of OR from left-1 and right
        for (int i=k; i<=n-k; i++) {
            /*
                if cnt of max-nums, that can make up curr-OR is less than K,
                then we can't take that OR, so we will continue
            */
            for (int lft=1; lft < 128; lft++) {
                if (lftOR[i-1][lft][1] < k) continue;

                for (int rgt=1; rgt < 128; rgt++) {
                    if (rgtOR[i][rgt][1] < k) continue;
                    
                    ans = Math.max(ans, lft ^ rgt);//Take XOR of only valid ORs
                }
            }
        }

        return ans;
    }

    void update(int[][] arr, int less, int more) {
        if (arr[more][0] == 0) {    // if this OR is appearing first time
            arr[more][0] = arr[less][0] +1;
            arr[more][1] = arr[less][1] +1;
        } else {    // otherwise update
            arr[more][0] = Math.min(arr[more][0], arr[less][0]+1);
            arr[more][1] = Math.max(arr[more][1], arr[less][1]+1);
        }
    }
}