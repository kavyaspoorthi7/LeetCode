class Solution:
    def maxDepthAfterSplit(self, seq):
        n = len(seq)
        maxDepth = 0
        depth = 0
        for c in seq:
            if c == ')':
                depth -= 1
                continue
            depth += 1
            if depth > maxDepth:
                maxDepth = depth

        r = [0] * n
        half = maxDepth >> 1

        depth = 0
        for i in range(n):
            c = seq[i]
            if c == ')':
                # Close A first if A has open
                if depth > 0:
                    depth -= 1
                    continue
                r[i] = 1
                continue
            # A is full, rest goes to B
            if depth >= half:
                r[i] = 1
                continue
            depth += 1
        return r