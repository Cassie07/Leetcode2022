class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        left = []
        right = []
        
        for i in s:
            if i.isalpha():
                continue
            elif i == '(':
                left.append(i)
            else:
                if left:
                    left.pop()
                else:
                    right.append(i)
        
        return len(left) + len(right)
