class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> currNums;
        for(int x : nums) {
            if(currNums.find(x) != currNums.end()) {
                return true;
            }
            currNums.insert(x);
        }
        return false;
    }
};