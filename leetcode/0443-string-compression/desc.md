## notes
- the submition on leetcode checks the chars array, so even a brute-force solution needs to modify it in place
- popping wouldn't be good because it shifts the array

## solutions
### two-pointer -ish
- create a pointer i = 0 and ins = 0 - ins keeps track of where we insert and stores the result
- while i is less than len(chars):
    - find the length of the current group of consecutive chars
    - add chars[i] to the answer (chars[ins] == chars[i]), increase the ins pointer
    - if group length is > 1, add the string repr of the group length
    - increase pointer i by group length and continue with the next group
- complexity:
    - time: O(n) - single pass
    - space: O(1) - modifying in place