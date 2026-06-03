class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for word in s:
            if word.isalnum():
                cleaned += word.lower()

        return cleaned == cleaned[::-1]
        