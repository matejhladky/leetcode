#include <iostream>

using namespace std;

// two pointer
string mergeAlternately(string word1, string word2) {
    int m = word1.size();
    int n = word2.size();
    string result = "";
    int i = 0;
    int j = 0;

    while (i < m || j < n) {
        if (i < m) {
            result.push_back(word1[i++]);
        }
        if (j < n) {
            result.push_back(word2[j++]);
        }
    }

    return result;
}

// one pointer
string mergeAlternately(string word1, string word2) {
    int n = max(word1.size(), word2.size());
    string result = "";
    for (int i = 0; i < n; i++) {
        if (i < word1.size()) {
            result.push_back(word1.at(i));
        }
        if (i < word2.size()) {
            result.push_back(word2.at(i));
        }
    }
    return result;
}
