#needs work, keep improving
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sort
        nums = mergesort(nums)
        #we can assume already ordered
        #find pairs
        top = len(nums)-1
        bottom = 0
        for i, num in enumerate(nums):
            while top > bottom:
                middle = int((top-bottom)/2)#round down
                if nums[middle] < target - num:
                    bottom = middle
                elif nums[middle] > target - num:
                    top = middle
                else: 
                    return [i,middle]
    
def merge( left, right): 
    if not len(left) or not len(right): 
        return left or right 

    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 

    return result 

def mergesort( list): 
    if len(list) < 2: 
        return list

    middle = int(len(list)/2)
    left = mergesort(list[:middle]) 
    right = mergesort(list[middle:]) 

    return merge(left, right) 
        
        
