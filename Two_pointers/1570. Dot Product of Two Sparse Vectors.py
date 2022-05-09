# two pointers
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
        self.nums_list = [(index, i) for index,i in enumerate(nums) if i !=0]
        print(self.nums_list)
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        p, q = 0, 0
        while p < len(self.nums_list) and q < len(vec.nums_list):
            if self.nums_list[p][0] == vec.nums_list[q][0]:
                res += self.nums_list[p][1] * vec.nums_list[q][1]
                p += 1
                q += 1
            elif self.nums_list[p][0] < vec.nums_list[q][0]:
                p += 1
            else:
                q += 1
        return res
# Simple
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i,j in zip(self.nums, vec.nums):
            res += i * j
