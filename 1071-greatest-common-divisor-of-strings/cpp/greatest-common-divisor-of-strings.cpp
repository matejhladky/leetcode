#include <iostream>

using namespace std;

// brute-force
bool valid(string str1, string str2, int k) {
    int len1 = str1.size();
    int len2 = str2.size();
    if (len1 % k != 0 || len2 % k != 0) {
        return false;
    }
    else {
        string base = str1.substr(0, k);
        int n1 = len1 / k;
        int n2 = len2 / k;
        return str1 == joinWords(base, n1) && str2 == joinWords(base, n2);
    }
}

string joinWords(string str, int k) {
    string result = "";
    for (int i = 0; i < k; i++) {
        result += str;
    }
    return result;
}

string gcdOfStrings(string str1, string str2) {
    int len1 = str1.size();
    int len2 = str2.size();

    for (int i = min(len1, len2); i >= 1; i--) {
        if (valid(str1, str2, i)) {
            return str1.substr(0, i);
        }
    }
    return "";
}

// GCD
string gcdOfStrings(string str1, string str2) {
    if (str1 + str2 != str2 + str1) {
        return "";
    }

    int gcdLength = gcd(str1.size(), str2.size());
    return str1.substr(0, gcdLength);
}