## solutions
### 1. brute-force
- nested loops iterating over pairs of elements
- complexity:
    - time: O(n^2)
    - space: O(1) - doesn't depend on the input size

### 2. hashmap
- iterate only once
- for each element, check if the complement has been seen
- if not, add the current item to the map
- complexity:
    - time: O(n) - traverse only once, lookup is constant
    - space: O(n) - exactly n elements are stored in the hashmap
