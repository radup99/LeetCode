class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opposite = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                ch2 = opposite[ch]
                if len(stack) < 1:
                    return False
                if stack[-1] != ch2:
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        return True
