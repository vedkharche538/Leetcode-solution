"""_summary_: First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

"""


def first_missing_positive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n) time and O(1) space
    # 1. Sort the array
    # 2. Check if the array is sorted
    # 3. Check if the array has any missing positive integers
    # 4. Return the smallest missing positive integer
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    first_missing_positive(nums)
