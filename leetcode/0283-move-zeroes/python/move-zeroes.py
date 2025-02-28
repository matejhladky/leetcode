# original solution, doesn't work
def a_moveZeroes(nums):
    if len(nums) != 1:
        curr = 0
        for i, num in enumerate(nums):
            if num != 0 and i != 0:
                nums[curr] = num
                curr += 1
                nums[i] = 0
    print(nums)

# space sub-optimal
def a_moveZeroes(nums):
    numZeroes = len([num for num in nums if num == 0])
    ans = [num for num in nums if num != 0]
    nums = ans + ([0] * numZeroes)
    print(nums)

# space optimal, operations sub-optimal
def b_moveZeroes(nums):
    lastNonZeroPos = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[lastNonZeroPos] = nums[i]
            lastNonZeroPos += 1
    
    for i in range(lastNonZeroPos, len(nums)):
        nums[i] = 0

# optimal
def c_moveZeroes(nums):
    lastNonZeroPos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            tmp = nums[lastNonZeroPos]
            nums[lastNonZeroPos] = nums[i]
            nums[i] = tmp
            lastNonZeroPos += 1

print(a_moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
# print(moveZeroes([0]), [0])
# print(moveZeroes([1]), [1])
# print(moveZeroes([1, 0]), [1, 0])