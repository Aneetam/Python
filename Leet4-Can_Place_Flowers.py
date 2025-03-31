def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if n == 0:
            return True  # No more flowers need to be planted
        
        if flowerbed[i] == 0:  # Check if the current spot is empty
            left_empty = (i == 0 or flowerbed[i - 1] == 0)  # Check left neighbor
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)  # Check right neighbor
            
            if left_empty and right_empty:  # If both sides are empty, plant a flower
                flowerbed[i] = 1  # Plant the flower
                n -= 1  # Reduce the number of flowers to be planted
    
    return n == 0  # If all flowers are planted, return True; otherwise, False

# Taking user input
flowerbed = list(map(int, input("Enter the flowerbed (comma-separated 0s and 1s): ").split(',')))
n = int(input("Enter the number of flowers to plant: "))

# Printing result
print("Output:", canPlaceFlowers(flowerbed, n))