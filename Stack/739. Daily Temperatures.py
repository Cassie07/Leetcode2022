class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 for i in temperatures]
        
        
        for index,temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = index - prev_index
            stack.append([temp,index])
        return res
