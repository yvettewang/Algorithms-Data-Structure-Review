# The classic version of binary search
def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) / 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

"""
    Binary search in 2D space, return the position of the target
    1 2   3  4
    5 6   7  8
    9 10 11 12
    target == 6
"""
def binary_search_2d_space(matrix, target):
    left = 0
    row = len(matrix)
    col = len(matrix[0])
    right = row * col - 1
    while left <= right:
        mid = left + (right - left) / 2
        r = mid / col
        c = mid % col
        if matrix[r][c] == target:
            return [r, c]
        if matrix[r][c] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]

# matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# print(binary_search_2d_space(matrix, 14))

"""
    Find an element in the array that is closest to the target number.
    1 2 3 8 9  target == 4  return:2
"""
def find_closest(nums, target):
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        m = l + (r - l) / 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m
        else:
            r = m
    # post-processing
    if abs(target - nums[l]) > abs(target - nums[r]):
        return r
    return l

'''
    Return the index of the first occurrence of an element.
    4 5 5 5 5 5 5 5 5   target == 5  return: 1
'''
def get_first_occurrence(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r - l) / 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    if nums[l] == target:
        return l
    return -1

'''
    Return the index of the last occurrence of an element.
    4 5 5 5 6 6 7   target == 5  return 3
'''
def get_last_occurrence(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + (r - l) / 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        elif nums[m] == target:
            if nums[m + 1] == target:
                l = m + 1
            else:
                return m
    if nums[l] == target:
        return l
    return -1

nums = [4,5,5,5,6,6,7]
print(get_first_occurrence(nums, 5))
print(get_last_occurrence(nums, 7))
