# solution 1 and 2
def canPlaceFlowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]  # pad
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
            if n <= 0:  # early return
                return True
    return n <= 0


# solution 3 (editorial)
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

    return count >= n

# solution 4 (formula)
def canPlaceFlowers(flowerbed, n):
    padded = [0] + flowerbed + [0]
    max_flowers = 0
    consecutive = 0 
    for plot in padded:
        if plot == 0:
            consecutive += 1
        else:
            max_flowers += (consecutive - 1) // 2
            consecutive = 0

    return max_flowers >= n



print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(canPlaceFlowers([0, 0, 1, 0], 1))
