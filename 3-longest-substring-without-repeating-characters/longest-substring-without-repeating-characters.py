class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1: return 0
        ls=1
        ss=s[0]
        for i in range(1,len(s)):
            while s[i] in ss:
                ss=ss[1:]
            ss+=s[i]
            ls=max(ls,len(ss))
        return ls
            

