#include <iostream>
#include <vector>

using namespace std;

// space sub-optimal
void moveZeroes(vector<int>& nums) {
    int numZeroes = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 0) {
            numZeroes++;
        }
    }
    vector<int> ans;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            ans.push_back(nums[i]);
        }
    }
    while (numZeroes--) {
        ans.push_back(0);
    }

    // will only work with vectors
    nums = ans;
}

// optimal space, sub-optimal operations
void moveZeroes(vector<int>& nums) {
    int lastNonZeroPos = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroPos++] = nums[i];
        }
    }
    for (int i = lastNonZeroPos; i < nums.size(); i++) {
        nums[i] = 0;
    }
}

// optimal
void moveZeroes(vector<int>& nums) {
    int lastNonZeroPos = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            swap(nums[lastNonZeroPos++], nums[i]);
        }
    }
}