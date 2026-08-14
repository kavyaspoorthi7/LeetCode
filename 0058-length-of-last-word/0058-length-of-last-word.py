class Solution(object):
    def lengthOfLastWord(self, s):
        w=s.strip().split()
        if not w:
            return 0
        return len(w[-1])