class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        
        prev = ''
        for i in s:
            if stack:
                prev = stack.pop()
                if prev != i:
                    stack.append(prev)
                    stack.append(i)
            else:
                stack.append(i)
            
        return ''.join(stack)
