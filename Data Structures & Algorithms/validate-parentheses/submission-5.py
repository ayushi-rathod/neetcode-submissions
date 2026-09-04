class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ']':'[',')':'('}
        stack = []
        for ch in s:
            if ch in hmap:
                if not stack or not stack[-1] == hmap[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0
