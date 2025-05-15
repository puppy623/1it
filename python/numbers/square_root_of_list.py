#square root of every number in list
import math
def square_root_of_list(numbers):
    return [math.sqrt(num) for num in numbers]

numbers = [1, 4, 9, 16, 25]
square_roots = square_root_of_list(numbers)
print("Original list:", numbers)
print("Square roots:", square_roots)