class Solution:
    def findMinLengthWords(self, strs: List[str]) -> List[str]:
        minWords = [strs[0]]
        minLen = len(strs[0])

        for st in strs[1:]:
            if len(st) < minLen:
                minWords = [st]
                minLen = len(st)
            elif len(st) == minLen:
                minWords.append(st)

        return minWords


    def longestCommonPrefix(self, strs: List[str]) -> str:
        minWords = self.findMinLengthWords(strs)
        for mw in minWords:
            while mw != "":
                valid = True
                for st in strs:
                    if not st.startswith(mw):
                        valid = False
                        continue
                if valid:
                    return mw
                mw = mw[:-1]
        return ""
