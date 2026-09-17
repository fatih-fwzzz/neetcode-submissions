import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return new_str == new_str[::-1]