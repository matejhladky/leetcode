#include <iostream>
#include <vector>
#include <limits>

using namespace std;

bool increasingTriplet(vector<int>& nums) {
    int first = numeric_limits<int>::max();
    int second = numeric_limits<int>::max();
    for (int num : nums) {
        if (num <= first) {
            first = num;
        } else if (num <= second) {
            second = num;
        } else {
            return true;
        }
    }
    return false;
}