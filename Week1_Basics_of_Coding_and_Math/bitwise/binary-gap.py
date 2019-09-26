class Solution:
    def binaryGap(self, N: int) -> int:
        N = bin(N)[2:]
        oneLocs = [i for i in range(len(N)) if N[i] == '1']
        if len(oneLocs) < 2:
            return 0
        maxim = -1
        for i in range(len(oneLocs)-1):
            maxim = max(maxim, oneLocs[i+1]-oneLocs[i])
        return maxim