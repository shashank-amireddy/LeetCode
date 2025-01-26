class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n  = digits.size();
        digits[n-1]++;
        for(int i = n-1; i>=0;i-- ){
            if(digits[i] == 10){
                digits[i] = 0;
                if(i-1>=0 ){
                    digits[i-1]++;
                }
                else{
                    digits.push_back(0);
                    digits[i]++;
                }
            }
        }
        return digits;
    }
};