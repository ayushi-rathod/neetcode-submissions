class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for ch in s:

            if ch in hmap:
                top_element = stack.pop() if stack else "#"

                if hmap[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack