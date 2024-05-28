class Solution {
    
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        Map<Integer, Integer> nm = new HashMap<>();
        for(int i : nums2)
        {
            int val = i * k;
            nm.put(val, nm.getOrDefault(val, 0) + 1);
        }
        long ans=0;
        for(int i : nums1)
        {
            for(int j=1;j*j<=i;j++)
            {
                if(i%j==0)
                {
                    if(nm.containsKey(j))
                    {
                        ans += nm.get(j);
                    }
                    int val=i/j;
                    if(j!=val && nm.containsKey(val))
                    {
                        ans += nm.get(val);
                    }
                }
            }
        }
        return ans;
    }
    
    // public long numberOfPairs(int[] nums1, int[] nums2, int k) {
    //     int m = nums1.length;
    //     int n = nums2.length;
        
    //     for (int i=0;i<n;i++) {
    //         nums2[i] *= k;
    //     }
        
    //     Map<Integer, Long> map1 = new HashMap<>();
    //     Map<Integer, Long> map2 = new HashMap<>();
        
    //     for (int i=0;i<m;i++) {
    //         map1.put(nums1[i] ,map1.getOrDefault(nums1[i], 0L) + 1);
    //     }
        
    //     for (int i=0;i<n;i++) {
    //         map2.put(nums2[i], map2.getOrDefault(nums2[i], 0L) + 1);
    //     }
        
    //     int p = map1.size();
    //     int q = map2.size();
        
    //     int[] arr1 = new int[p];
    //     int[] arr2 = new int[q];
        
    //     int a = 0;
    //     for (Integer key: map1.keySet()) {
    //         arr1[a] = key;
    //         a++;
    //     }
        
    //     a = 0;
    //     for (Integer key: map2.keySet()) {
    //         arr2[a] = key;
    //         a++;
    //     }
        
    //     long count = 0;
        
    //     Arrays.sort(arr1);
    //     Arrays.sort(arr2);
        
    //     for (int i = 0;i<q;i++) {
    //         int ind = findIndex(0, p-1, arr1, arr2[i]);
    //         if (arr1[ind] >= arr2[i]) {
    //             for (int j =ind;j<p;j++) {
    //                 if (arr1[j] % arr2[i] == 0) {
    //                     //System.out.println(map1.get(arr1[j]) + " " + map2.get(arr2[i]));
    //                     count += (long)((map1.get(arr1[j]) * map2.get(arr2[i])));
    //                 }
    //             }
    //         } else {
    //             break;
    //         }
    //     }
        
    //     return count;
    // }
    
    // private int findIndex(int start, int end, int[] arr, int target) {
        
    //     while (start < end) {
    //         int mid = start + (end - start)/2;
            
    //         if (arr[mid] == target) {
    //             return mid;
    //         } else if (arr[mid] < target) {
    //             start = mid + 1;
    //         } else {
    //             end = mid;
    //         }
    //     }
    //     return end;
    // }
}