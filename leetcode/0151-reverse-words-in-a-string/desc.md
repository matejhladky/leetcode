## solutions
- the point of the second solution is the two pointer technique to achieve O(1) space -> requires mutable strings

### 1. split then join in reverse
- complexity:
    - time: O(n)
    - space: O(n) - creating new array

### 2. two pointer in-place
- reverse the string
- set the pointers - left, right and index
- keep iterating until we find non-space
- then keep increasing the right pointer till the end of the word
- reverse the found word
- set the left pointer to right's position and repeat
- skip last empty characters
- complexity:
    - time: O(n)
    - space: O(1)