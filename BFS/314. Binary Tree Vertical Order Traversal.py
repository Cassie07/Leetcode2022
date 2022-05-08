class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columnTable = collections.defaultdict(list)
        queue = deque([(root, 0)])
        
        while queue:
            node, column = queue.popleft()
            
            if node:
                columnTable[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append((node.right, column+1))
        
        return [columnTable[i] for i in sorted(columnTable.keys())]
