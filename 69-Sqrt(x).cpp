class Solution {
public:
    int mySqrt(int x) {
        if(x < 2){
            return x;
        }
        int lo = 1, hi = x, res = 1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            long long mid_squared = (long long)mid * mid;  // Use long long to avoid overflow
            if(mid_squared <= x) {
                res = mid;
                lo = mid + 1;
            }
            else {
                hi = mid - 1;
            }
        }
        return res;
    }
};
