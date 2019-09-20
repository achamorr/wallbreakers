class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        new_A = []
        for j in range(len(A)):
            row = A[j]
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:   #we only have 1 or 0
                    row[i] = 0
            A[j] = reversed(row)
        return A
                    