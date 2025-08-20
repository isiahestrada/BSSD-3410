import timeit
import random

def search(arr, n, x):
    # Iterate over the array in order to
    # find the key x
    operations = 0
    for i in range(0, n):
        operations += 1
        if (arr[i] == x):
            print("linear ops:", operations)
            return i
    print("linear ops:", operations)
    return -1


def binarySearch(arr, low, high, x):
    operations = 0
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        operations += 1
        if arr[mid] == x:
            print("binary ops:", operations)
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    print("binary ops:", operations)
    return -1

if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(200)]
    arr.sort()
    print("arr length:", len(arr))
    x = random.choice(arr)

    low = 0
    high = len(arr) - 1

    iter = 10
    ltime = timeit.timeit(lambda:search(arr, len(arr),x), setup="from __main__ import search", number=iter)
    btime = timeit.timeit(lambda:binarySearch(arr, low, high, x), setup="from __main__ import binarySearch", number=iter)

    print(f"Searching for: {x}")
    print(f"Linear search took: {ltime}")
    print(f"Binary search took: {btime}")