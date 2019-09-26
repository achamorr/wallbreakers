#come back to ,needs work

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        groups = list()
        candidates = list()
        for i in range(len(M)):
            for j in range(i+1): #only look through half
                if M[i][j] == 1:
                    candidates.append([i,j])
        #group together
        removeList = list()
        lastRunLength = -1
        while len(candidates) != lastRunLength:
            for item in candidates:
                union = list(set(item) | set(item_compare))
                if len(union) < len(item)+len(item_compare):
                    removeList.append(item)
                    removeList.append(item)

                    candidates.append(union)

            candidates.remove(group)