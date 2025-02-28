


    Initialize lastNonZeroFoundAt to 0 to track the position of the last non-zero element.

    Iterate through each element in nums using cur as the index:
        If nums[cur] is not zero:
            Swap nums[lastNonZeroFoundAt] with nums[cur] to move the non-zero element to the correct position.
            Increment lastNonZeroFoundAt to update the position for the next non-zero element.

    Continue iterating until all elements are processed, ensuring all non-zero elements are moved to the front of the array and zeros are pushed to the end.


## notes
- for some reason, leetcode won't accept the sub-optimal solution even though it works (i guess the array doesn't get overwritten)
- had the correct idea, just didn't swap them (overwrote them instead)

## solutions
### 1. sub-optimal space
- count the number of zeros
- create a new array, append all the nonzero elements
- add 0 * numZeroes at the end
- rewrite the original array with the new array
- complexity:
    - time: O(n)
    - space: O(n) - extra array with the same size

### 2. space optimal, operations sub-optimal
- iterate through the array and keep track of the last non-zero element (lastNonZeroPos)
- if a non-zero element is found, place it at the lastNonZeroPos index, increment the index
- then fill the rest of the array with zeros (from lastNonZeroPos to the end of the array) 
- complexity:
    - time: O(n) - worst-case i O(2n), however the total number of operations (array writes) is n (e.g. [0, 0, 0, ..., 0])
    - space: O(1)

### 3. optimal
- similar as before - keep track of last non-zero element
- iterate through the array, once non-zero is encountered, swap nums[i] and nums[lastNonZeroPos], increment lastNonZeroPos
- complexity:
    - time: O(n) - optimal number of operations, which is the number of non-zero elements
    - space: O(1)