class Solution {
    public void addBits(int[] bits, int n) {
        for (int i = 31;i>=0;i--) {
            bits[i] += ((n>>i) & 1);
        }
    }

    public void removeBits(int[] bits, int n) {
        for (int i = 31;i>=0;i--) {
            bits[i] -= ((n>>i) & 1);
        }
    }

    public int calculateAnd(int[] bits, int len) {
        int r = 0;
        int p = 1;

        for (int i=0;i<32;i++) {
            // All bits are set in this length, add the corresponding bit value to the result
            // as the bitwise AND will be 1 at this bit.
            if (bits[i] == len) {
                r += p;
            }
            p = p*2; // left shifting p to move to next bit.
        }

        return r;
    }

    public int minimumDifference(int[] nums, int k) {
        int[] bits = new int[32];
        int min = Integer.MAX_VALUE, left = 0, right = 0;

        while (right < nums.length) {
            addBits(bits, nums[right]);
            int currAnd = calculateAnd(bits, right - left + 1);
            min = Math.min(min, Math.abs(k - currAnd));
            // Bitwise And will either be the same or decrease as we add more numbers.
            // So we re removing the numbers from the left until either we reach to a single element.
            // or we get a greater bitwise AND than k. As greater AND can be reduced by adding more numbers.
            // but smaller AND will only decrease thereby increasing abs(k - bitwiseAnd) 
            while (left <= right && currAnd < k) {
                removeBits(bits, nums[left++]);
                currAnd = calculateAnd(bits, right - left + 1);
                min = Math.min(min, Math.abs(k - currAnd));
            }
            // Increasing the window.
            right++;
        }

        return min;
    }
}