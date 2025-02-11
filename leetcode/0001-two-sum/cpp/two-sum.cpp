#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
    int n = nums.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                return {i, j};
            }
        }
    }
    return {};
}

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> hashMap;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        int complement = target - nums[i];
        if (hashMap.count(complement)) {
            return {hashMap[complement], i};
        }
        hashMap[nums[i]] = i;
    }
    return {};
}