class Solution:
    def simplifyPath(self, path: str) -> str:
        
        res = []
        stack = []
        for content in path.split('/'):
            if content == '' or content =='.':
                continue
            elif content == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(content)
        
        s = '' 
        if stack:
            for i in stack:
                s += '/' + i
            return s
        else:
            return '/'
