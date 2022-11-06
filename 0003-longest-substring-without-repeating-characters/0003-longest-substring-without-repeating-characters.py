class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1
        charset = set()
        res = 0
        left = 0
        for i in range(len(s)):
            while(s[i] in charset):
                charset.remove(s[left])
                left += 1
            charset.add(s[i])
            res = max(res, i-left+1)
        return res
