class Solution:
    def isValid(self, s: str) -> bool:
        parent = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                parent.append(char)
            else:
                if not parent:
                    return False
                if char == ')' and parent[-1] == '(':
                    parent.pop()
                elif char == '}' and parent[-1] == '{':
                    parent.pop()
                elif char == ']' and parent[-1] == '[':
                    parent.pop()
                else:
                    return False

        return len(parent) == 0