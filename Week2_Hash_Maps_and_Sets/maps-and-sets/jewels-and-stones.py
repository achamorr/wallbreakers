class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelsMined = [s for s in S if (s in J)]
        return len(jewelsMined)