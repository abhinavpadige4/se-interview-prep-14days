"""
Problem: Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
Difficulty: Medium
Topics: Sliding Window, Array, Binary Search

Solution:
We use a sliding window approach with two pointers (left and right).
Expand the window by moving right pointer and adding elements to current sum.
When current sum >= target, shrink the window from left to find the minimum size.
Update the minimum length whenever we find a valid window.

Time Complexity: O(n) where n is the number of elements in the array.
Space Complexity: O(1) - only using two pointers and variables.
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_sum = 0
        min_length = float('inf')
        n = len(nums)
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_length == float('inf') else min_length