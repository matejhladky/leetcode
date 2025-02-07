## notes
- in python, appending to a string isn't as efficient as putting chars in an array and then using ``"".join()``

## solutions
### 1. two pointers
- create two pointers and iterate until either of them points at the end of each word
- then append the rest of the string
- time: O(m + n) - m, n are the lengths of each word; we have to visit each character
- space: O(1) - not considering the space of input and output

### 2. one pointer
- can use one pointer by iterating till the length of the longer word
- then, in the loop, checking if we are in bounds
- time: O(m + n) - same as before
- space: O(1) - same as before

