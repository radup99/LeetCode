class Solution:
    def get_letter_count(text):
        count = {}
        for ch in text:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 0
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Solution.get_letter_count(s)
        count_t = Solution.get_letter_count(t)
        return True if count_s == count_t else False
