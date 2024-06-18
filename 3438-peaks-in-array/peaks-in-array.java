/**
https://leetcode.com/problems/peaks-in-array/solutions/5319870/segment-tree-solution-beat-1000
 */
class SegmentTree {
    int[] arr;
    int[] tree;
    int n;

    public SegmentTree(int[] arr) {
        this.arr = arr;
        this.n = arr.length;
        this.tree = new int[4 * n];
        build(0, 0, n - 1);
    }

    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = isGreaterThanAdjacent(start) ? 1 : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    private boolean isGreaterThanAdjacent(int index) {
        boolean leftCheck = (index == 0) || (arr[index] > arr[index - 1]);
        boolean rightCheck = (index == n - 1) || (arr[index] > arr[index + 1]);
        return leftCheck && rightCheck;
    }

    public int query(int L, int R) {
        return query(0, 0, n - 1, L, R);
    }

    private int query(int node, int start, int end, int L, int R) {
        if (R < start || end < L) {
            return 0;
        }
        if (L <= start && end <= R) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int leftQuery = query(2 * node + 1, start, mid, L, R);
        int rightQuery = query(2 * node + 2, mid + 1, end, L, R);
        return leftQuery + rightQuery;
    }

    public void update(int index, int value) {
        arr[index] = value;
        update(0, 0, n - 1, index);
        // Update the adjacent elements that might be affected by the change
        if (index > 0) {
            update(0, 0, n - 1, index - 1);
        }
        if (index < n - 1) {
            update(0, 0, n - 1, index + 1);
        }
    }

    private void update(int node, int start, int end, int index) {
        if (start == end) {
            tree[node] = isGreaterThanAdjacent(index) ? 1 : 0;
        } else {
            int mid = (start + end) / 2;
            if (start <= index && index <= mid) {
                update(2 * node + 1, start, mid, index);
            } else {
                update(2 * node + 2, mid + 1, end, index);
            }
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }
}

class Solution {
    public List<Integer> countOfPeaks(int[] arr, int[][] q) {
        SegmentTree t = new SegmentTree(arr);
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < q.length; i++) {
            if (q[i][0] == 1) {
                ans.add(t.query(q[i][1] + 1, q[i][2] - 1));
            } else {
                t.update(q[i][1], q[i][2]);
            }
        }
        return ans;
        
    }
}

/**
Square Root Decomposition 
https://leetcode.com/problems/peaks-in-array/solutions/5320380/sqrt-decomposition-n-sqrt-n
 */

// class Solution {
//     public List<Integer> countOfPeaks(int[] aa, int[][] q) {
//         int n=aa.length;
//         int a[] = new int[n+1];
//         for(int i=0;i<n;i++)a[i+1]=aa[i];
//         int rootn = (int)Math.sqrt(n);
//         int parts = n/rootn;
//         int rem = n%rootn;
//         if(rem>0)parts++;
//         int sd[] = new int[parts+1];
//         for(int i=1;i<=n;i++){
//             int ind = getSDIndex(n, rootn, i);
//             int lind = getPartitionLastIndex(n,rootn,i);
//             int find = getPartitionFirstIndex(n,rootn,i);
//             if(i==lind || i==find)continue;
//             sd[ind]+=(a[i]>a[i-1] && a[i]>a[i+1] ? 1 : 0);
//         }
//         List<Integer>ans = new ArrayList<>();
//         int m=q.length;
//         for(int i=0;i<m;i++){
//             int t=q[i][0];
//             if(t==1){
//                 int l=q[i][1], r=q[i][2];
//                 l++;r++;
//                 int x = getRangeQueryAnswer(l+1,r-1,a,sd,n,rootn);
//                 ans.add(x);
//             }
//             else {
//                 int ind2 = q[i][1];
//                 int val = q[i][2];
//                 ind2++;
//                 for(int ii=ind2-1;ii<=ind2+1;ii++){
//                     if(ii>n || ii<1)continue;
//                     int ind = getSDIndex(n, rootn, ii);
//                     int lind = getPartitionLastIndex(n,rootn,ii);
//                     int find = getPartitionFirstIndex(n,rootn,ii);
//                     if(ii==lind || ii==find)continue;
//                     sd[ind]-=(a[ii]>a[ii-1] && a[ii]>a[ii+1] ? 1 : 0);
//                 }
//                 a[ind2]=val;
//                 for(int ii=ind2-1;ii<=ind2+1;ii++){
//                     if(ii>n || ii<1)continue;
//                     int ind = getSDIndex(n, rootn, ii);
//                     int lind = getPartitionLastIndex(n,rootn,ii);
//                     int find = getPartitionFirstIndex(n,rootn,ii);
//                     if(ii==lind || ii==find)continue;
//                     sd[ind]+=(a[ii]>a[ii-1] && a[ii]>a[ii+1] ? 1 : 0);
//                 }
//             }
//         }
//         return ans;
//     }
    
//     private static int getRangeQueryAnswer(int l, int r, int a[], int sd[], int n, int rootn){
//         int ans = 0;
//         if(l>r || l>n || r>n)return 0;
//         if(getSDIndex(n, rootn, l) == getSDIndex(n, rootn, r)){
//             for(int i=l;i<=r;i++){
//                 if(a[i]>a[i-1] && a[i]>a[i+1])ans++;
//             }
//             return ans;
//         }
//         int lastIndexOfL = getPartitionLastIndex(n, rootn, l);
//         for(int i=l;i<=lastIndexOfL;i++){
//             if(a[i]>a[i-1] && a[i]>a[i+1])ans++;
//         }
//         int startInd = getSDIndex(n, rootn, l);
//         startInd++;
//         int endInd = getSDIndex(n, rootn, r);
//         endInd--;
//         for(int i=startInd;i<=endInd;i++){
//             int find = getPartitionFirstIndex2(n,rootn,i);
//             if(find-1>=l-1 && find+1<=r+1){
//                 if(a[find]>a[find-1] && a[find]>a[find+1])ans++;
//             }
//             int lind = getPartitionLastIndex2(n,rootn,i);
//             if(lind+1<=r+1 && lind-1>=l-1){
//                 if(a[lind]>a[lind-1] && a[lind]>a[lind+1])ans++;
//             }
//             ans+=sd[i];
//         }
//         int firstIndexOfR = getPartitionFirstIndex(n, rootn, r);
//         for(int i=firstIndexOfR;i<=r;i++){
//             if(a[i]>a[i-1] && a[i]>a[i+1])ans++;
//         }
//         return ans;
//     }
    
//     private static int getSDIndex(int n, int rootn, int i){
//         int x = i%rootn;
//         if(x==0)x=rootn;
//         int ind = (i - x)/rootn + 1;
//         return ind;
//     }

//     private static int getPartitionLastIndex(int n, int rootn, int i) {
//         int ind = getSDIndex(n, rootn, i);
//         return Math.min(ind*rootn,n); 
//         // min is used to handle the last partition of size < rootn
//     }

//     private static int getPartitionFirstIndex(int n, int rootn, int i) {
//         int ind = getSDIndex(n, rootn, i);
//         return (ind-1)*rootn + 1;
//     }
    
//     private static int getPartitionLastIndex2(int n, int rootn, int i) {
//         // int ind = getSDIndex(n, rootn, i);
//         return Math.min(i*rootn,n); 
//         // min is used to handle the last partition of size < rootn
//     }

//     private static int getPartitionFirstIndex2(int n, int rootn, int i) {
//         // int ind = getSDIndex(n, rootn, i);
//         return (i-1)*rootn + 1;
//     }
// }