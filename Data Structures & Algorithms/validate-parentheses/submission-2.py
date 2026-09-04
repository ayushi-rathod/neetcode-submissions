class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ']':'[',')':'('}
        stack = []
        for ch in s:
            if stack and stack[-1] == '{' and ch == '}':
                stack.pop()
            elif stack and stack[-1] == "(" and ch == ')':
                stack.pop()
            elif stack and stack[-1] == "[" and ch == ']':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0
