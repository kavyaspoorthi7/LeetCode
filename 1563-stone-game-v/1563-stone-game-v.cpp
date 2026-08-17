class Solution {
public:
    int n;
    int t[501][501];

    int solve(int left, int right, vector<int>& prefixSum) {
        if (left >= right)
            return 0;

        if (t[left][right] != -1) {
            return t[left][right];
        }

        int leftsum = 0;
        int rightsum = 0;
        int score = 0;

        for (int mid = left; mid < right; mid++) {
            leftsum = prefixSum[mid + 1] - prefixSum[left];
            rightsum = prefixSum[right + 1] - prefixSum[mid + 1];

            if (leftsum < rightsum) {
                score = max(
                    score,
                    leftsum + solve(left, mid, prefixSum)
                );
            }
            else if (leftsum > rightsum) {
                score = max(
                    score,
                    rightsum + solve(mid + 1, right, prefixSum)
                );
            }
            else {
                score = max(
                    score,
                    max(
                        leftsum + solve(left, mid, prefixSum),
                        rightsum + solve(mid + 1, right, prefixSum)
                    )
                );
            }
        }

        return t[left][right] = score;
    }

    int stoneGameV(vector<int>& nums) {
        n = nums.size();

        memset(t, -1, sizeof(t));

        vector<int> prefixSum(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        return solve(0, n - 1, prefixSum);
    }
};