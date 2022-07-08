class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            cur_level = max(left, right) + 1
            dic[cur_level].append(root.val)
            
            return cur_level
        
        dic = collections.defaultdict(list)
        dfs(root)
        
        return [i for i in dic.values()]
