#include <iostream>
#include <vector>

using namespace std;

// brute-force
vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> answer;
    for (int i = 0; i < nums.size(); i++) {
        int product = 1;
        for (int j = 0; j < nums.size(); j++) {
            if (j != i) {
                product *= nums[j];
            }
        }
        answer.push_back(product);
    }
    return answer;
}

// not in place solution
vector<int> productExceptSelf(const vector<int>& nums) {
    int n = nums.size();
    vector<int> prefix(n, 1);
    vector<int> suffix(n, 1);
    for (int i = 1; i < n; ++i) {
        prefix[i] = prefix[i - 1] * nums[i - 1];
    }
    for (int i = n - 2; i >= 0; --i) {
        suffix[i] = suffix[i + 1] * nums[i + 1];
    }
    vector<int> result(n);
    for (int i = 0; i < n; ++i) {
        result[i] = prefix[i] * suffix[i];
    }
    return result;
}

// optimal solution
vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> answer(nums.size(), 1);
    int prefix = 1;
    for (int i = 0; i < nums.size(); i++) {
        answer[i] *= prefix;
        prefix *= nums[i];
    }
    int suffix = 1;
    for (int i = nums.size() - 1; i >= 0; i--) {
        answer[i] *= suffix;
        suffix *= nums[i];
    }
    return answer;
}


   vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n);
        output[0] = 1;
        for(int i=1; i<n; i++){
            output[i] = output[i-1] * nums[i-1];
        }
        int right = 1;
        for(int i=n-1; i>=0; i--){
            output[i] *= right;
            right *= nums[i];
        }
        return output;
    }

