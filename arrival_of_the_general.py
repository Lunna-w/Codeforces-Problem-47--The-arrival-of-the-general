n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

max_index = heights.index(max_height)
min_index = heights[::-1].index(min_height)

min_index = n - min_index - 1  

swaps = max_index  
if min_index > max_index:  
    swaps += n - 1 - min_index 
else:  
    swaps += n - 2 - min_index  

print(swaps)