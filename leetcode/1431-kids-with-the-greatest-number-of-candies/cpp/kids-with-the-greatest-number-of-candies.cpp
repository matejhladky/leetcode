#include <iostream>
#include <vector>

using namespace std;

vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    int maxVal = *max_element(candies.begin(), candies.end());
    vector<bool> result(candies.size());
    for (int i = 0; i < candies.size(); i++) {
        result[i] = candies[i] + extraCandies >= maxVal;
    }
    return result;
}