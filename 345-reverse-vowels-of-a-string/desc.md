## notes
- using set is better for O(1) access when checking for presense in vowels
- can use while instead of if-continue
- in C++, set is implemented with red-black tree (O(nlogn) lookup), so use unordered_set (O(1))

## solutions
### 1. two pointer
- set pointer at the beginning and end
- loop until they meet
- keep increasing each individually until a vowel is found
- then swap and move the pointers
- complexity:
    - time: O(n) - traversing the array once from each side
    - space: O(n) or O(1) if extra sting/array is created (immutable strings, e.g. Python and Java), otherwise constant (mutable strings, e.g. C++)