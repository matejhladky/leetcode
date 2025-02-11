def kidsWithCandies(candies, extraCandies):
    return [i + extraCandies >= max(candies) for i in candies]

print(kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies = 3))