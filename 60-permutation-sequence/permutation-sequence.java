class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder("");
        int[] fact = getFactorial(n);
        List<Integer> nums = new ArrayList<>();
        for (int i = 1;i<=n;i++) {
            nums.add(i);
        }
        while (k > 0) {
            int q = (k-1)/fact[n-1];
            // if (q == n) {
            //     sb.append(nums.get(nums.size() - 1));
            //     nums.remove(nums.size() - 1);
            //     break;
            // }
            if (n == 2 || n== 1) {
                q = k/fact[n-1];
                sb.append(nums.get(q-1));
                nums.remove(q-1);
            } else {
                sb.append(nums.get(q));
                nums.remove(q);
            }
            k = k % fact[n-1];
            n--;
        }

        if (!nums.isEmpty()) {
            Collections.sort(nums, Collections.reverseOrder());
            for (int i : nums) {
                sb.append(i);
            }
        }

        return sb.toString();

    }

    public int[] getFactorial(int n) {
        int[] fact =  new int[n+1];
        fact[0] = fact[1] = 1;

        for (int i =2;i<=n;i++) {
            fact[i] = fact[i-1] * i;
        }

        return fact;
    }
}