class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        new_array = []
        for i in range(len(A[0])):
            temp_arr = []
            for li in A:
                temp_arr.append(li[i])
            new_array.append(temp_arr)
        return new_array
            
            