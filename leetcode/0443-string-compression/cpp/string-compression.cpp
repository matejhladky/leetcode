#include <iostream>
#include <vector>

using namespace std;

int compress(vector<char>& chars) {
    int i = 0;
    int ins = 0;
    while (i < chars.size()) {
        int groupLength = 1;
        while (i + groupLength < chars.size() && chars[i + groupLength] == chars[i]) {
            groupLength++;
        }
        chars[ins] = chars[i];
        ins += 1;
        if (groupLength > 1) {
            for (char c : to_string(groupLength)) {
                chars[ins++] = c;
            }
        }
        i += groupLength;
    }
    return ins;
}