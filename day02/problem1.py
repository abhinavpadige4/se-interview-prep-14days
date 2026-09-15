"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topics: Two Pointers, String

Solution:
We use two pointers, one starting at the beginning and one at the end of the string.
We move the pointers towards each other, skipping non-alphanumeric characters.
At each step, we compare the characters (case-insensitive).
If they don't match, return False.
If the pointers cross, all characters matched, so return True.

Time Complexity: O(n) where n is the length of the string.
Space Complexity: O(1) - only using two pointers.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True