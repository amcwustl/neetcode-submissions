class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(word) - 1

        while left <= right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True