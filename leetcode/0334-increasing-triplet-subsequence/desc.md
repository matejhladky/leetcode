## notes
- the optimal solution is really based on the idea that we don't have to output the triplet
-> it keeps track of the values "implicitly" by the logic of the algorithm, it doesn't store them, which makes it kinda unintuitive (because it looks like the i < j < k condition is not satisfied)

## solutions
### 1. brute-force
- three loops, checking for the three values
- actually infeasible
- complexity:
    - time: O(n^3)
    - space: O(1)

### 2. keeping track of minimal values ("greedy")
- initialize first two numbers to inf
- for each number in the array:
    1. check if it's <= the current first number (if so, update)
    2. if not, check if it's <= the current second number (if so, update)
    3. if there is still a number and its bigger than second number, return true
- complexity:
    - time: O(n)
    - space: O(1)