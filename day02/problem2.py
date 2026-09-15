"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Topics: Two Pointers, Array, Sorting

Solution:
1. Sort the array.
2. Iterate through the array with index i.
3. For each i, use two pointers (left = i+1, right = len(nums)-1) to find pairs that sum to -nums[i].
4. Skip duplicate elements to avoid duplicate triplets.
5. If sum < 0, move left pointer right; if sum > 0, move right pointer left.

Time Complexity: O(n^2) where n is the number of elements.
Space Complexity: O(1) or O(n) depending on sorting algorithm (we use Timsort in Python).
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result