class Solution {
public:
    int searchInsert(vector<int>& nums, int k) {
        int start =0;
        int end = (nums.size() -1);
        int mid =0;
        while(start <= end){
            mid = (start+end)/2;
            if(nums[mid] == k) return mid;
            if(nums[mid] > k) end = mid-1;
            else start = mid+1;
        }
        return start;
    }
};