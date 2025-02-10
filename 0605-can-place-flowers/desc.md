## notes
- in the basic/greedy approach, to avoid manual handling of when len == 0, and the first + last element, the trick is to pad the input

## solutions
### 1. single pass
- pass through the array and check adjacent positions
- complexity:
    - time: O(n) - single pass through the array
    - space: O(n) - extra array is created (see solution 3)

### 2. single pass - optimized (early return)
- same as before, just return early if we hit the number of flowers
- complexity:
    - time: O(n) - single pass through the array
    - space: O(n) - extra array is created (see solution 3)

### 3. no additional space
- complexity:
    - time: O(n) - single pass through the array
    - space: O(1) - no extra array

### (extra) formula
- for any segment of consecutive zeros of length k, we can plant at most (k−1) // 2 new flowers without violating the adjacent rule.
- complexity:
    - time: O(n) - single pass through the array
    - space: O(n) - extra array is created