def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    
	# Traversing and saving parents
    def find_path(root):
        path = []
        while root != None:
            path.append(root)
            root = root.parent
        return path
    

    p_path = find_path(p)
    q_path = find_path(q)
    
    cur = -1
	# find the lowest common ancester
    for index,i in enumerate(p_path):
        if i in q_path:
            if cur == -1:
                cur = index
            if cur > index:
                cur = index 
    return p_path[cur]
