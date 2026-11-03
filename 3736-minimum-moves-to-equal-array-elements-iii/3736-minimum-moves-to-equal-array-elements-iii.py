class Fenwick:
    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.bit[i] += nums[i - 1]
            parent = i + (i & -i)
            if parent <= self.n:
                self.bit[parent] += self.bit[i]

    def update(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index

        return total

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minMoves(self, nums):
        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}
        freq = [0] * m
        sums = [0] * m
        for x in nums:
            i = pos[x] - 1
            freq[i] += 1
            sums[i] += x
        countBIT = Fenwick(freq)
        sumBIT = Fenwick(sums)

        max_idx = countBIT.kth(len(nums))
        maximum = vals[max_idx - 1]

        total = sumBIT.query(m)
        return len(nums) * maximum - total