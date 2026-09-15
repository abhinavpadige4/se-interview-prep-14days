"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topics: Array, Hash Table

Solution:
We use a hash table to store the value and its index as we iterate through the array.
For each element, we calculate the complement (target - current number) and check if it exists in the hash table.
If it does, we return the current index and the index of the complement.
If not, we add the current element and its index to the hash table.

Time Complexity: O(n) where n is the number of elements in the array.
Space Complexity: O(n) for the hash table.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash table to store the value and its index
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        # According to the problem statement, there is exactly one solution.
        return []