## notes
- the optimal solution is a bit hard to read with how the previous product is stored, here is a more readable solution which directly uses the previous element: 
https://leetcode.com/problems/product-of-array-except-self/solutions/3186745/best-c-3-solution-dp-space-optimization-brute-force-optimize-one-stop-solution

## solutions
### 1. brute-force
- iterate (j) through the array for every index i
- multiply the numbers when i != j
- append to the answer array
- complexity:
    - time: O(n^2)
    - space: O(1) - technically, if we don't count the output array 

### 2. division of the product
- get product of the entire array
- iterate through the array and divide by each element, append to the answer
-> efficitevly "eliminating" each index
- issue: if the array contains zero, it won't work
- complexity:
    - time: O(n)
    - space: O(1) - same reasoning as before

### 3. prefix and suffix product
- compute preffix and suffix:
    - each element at prefix[i] contains the product of all elements before i (reusing the previous calculations)
    - each element at suffix[i] contains the product of all elements after i (reusing the previous calculations)
- then multiply prefix by suffix - i.e. product of all elements before and after i, except i
- complexity:
    - time: O(n) - single sweep through the array (twice)
    - space: O(n) - two extra arrays

### 4. directly storing the prefix and suffix product
- this is an optimization of the previous solution to achive O(1) space
- it's the same, just in place:
    - we compute the prefix product and store it at that position
    -> each index stores the complete product up to that point
    - same for the suffix
- complexity:
    - time: O(n)
    - space: O(1)