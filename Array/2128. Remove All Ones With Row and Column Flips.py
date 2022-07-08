class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        
        row, row_flip = len(grid), [1-i for i in grid[0]]

        for i in range(row):
            if grid[i] != grid[0] and grid[i] != row_flip:
                return False
            
        return True
