# Simple version with O(n2) complexity

def find_two_sum(arr, target):
    """Returns indexes of two integers in an array that sums up to target value"""
    for i in range(len(arr)):
        for y in range(len(arr)):
            if y > i:
                if arr[i] + arr[y] == target:
                    return [i, y]
    return
