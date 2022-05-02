class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        left = []
        right = []
        
        for index,i in enumerate(s):
            
            if i.isalpha():
                continue
            elif i == '(':
                left.append(index)
            else:
                if len(left) == 0:
                    right.append(index)
                else:
                    left.pop()
        
        remove = left + right
        
        res = ''
        
        for index,i in enumerate(s):
            if index not in remove:
                res += i
            else:
                continue
        
        return res
