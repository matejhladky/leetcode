from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dct = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in dct:
            return [dct[complement], i]
        dct[nums[i]] = i
    return []

print(twoSum(None, nums=[2, 7, 11, 15], target=9))
print(twoSum(None, nums=[3, 2, 4], target=6))
print(twoSum(None, nums=[3, 3], target=6))
