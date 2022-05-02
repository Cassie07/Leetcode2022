class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []
        
        for index,i in enumerate(heights):
            stack.append((i, index))
        
        view = []
        cur = -1
        for i in range(len(stack)):
            num, index = stack.pop()
            if cur == -1:
                cur = num
                view.append(index)
            else:
                if num > cur:
                    cur = num
                    view.append(index)
                else:
                    continue
        
        return view[::-1]
