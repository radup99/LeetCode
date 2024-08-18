class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [w for w in s.split() if w.strip()]
        return len(words[-1])
