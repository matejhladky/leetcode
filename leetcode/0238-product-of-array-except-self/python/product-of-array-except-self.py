from math import prod

def a_productExceptSelf(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        answer.append(product)
    return answer

# same as before
def b_productExceptSelf(nums):
    answer = []
    for i in range(len(nums)):
        product = prod(nums[:i]) * prod(nums[i + 1:])
        answer.append(product)
    return answer

def c_productExceptSelf(nums):
    product = 1
    answer = []
    for n in nums:
        product *= n
    for n in nums:
        answer.append(int(product / n))
    return answer

def d_productExceptSelf(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    
    return [prefix[i] * suffix[i] for i in range(len(nums))]

def e_productExceptSelf(nums):
    answer = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        answer[i] *= prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer

print(e_productExceptSelf([1, 2, 3, 4]))