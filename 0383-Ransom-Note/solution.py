class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if r not in magazine:
                return False
            magazine = magazine.replace(r, "", 1)
        return True
