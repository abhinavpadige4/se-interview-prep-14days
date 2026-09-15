"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topics: Array, Hash Table

Solution:
We use a hash set to track the elements we have seen.
As we iterate through the array, if we encounter an element that is already in the set,
we return True (duplicate found). Otherwise, we add the element to the set.
If we finish the iteration without finding duplicates, return False.

Time Complexity: O(n) where n is the number of elements in the array.
Space Complexity: O(n) for the hash set.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False