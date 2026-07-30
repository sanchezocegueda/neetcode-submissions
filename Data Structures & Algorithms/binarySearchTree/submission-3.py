class TreeNode:
    def __init__(self, key: int, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        # print(f"Inserting {key}, {val}")
        # empty tree is easy
        if self.root is None:
            self.root = TreeNode(key, val)
            return # that's it

        # look for the key
        prev = None
        cur = self.root

        while cur is not None and cur.key != key:
            prev = cur
            # print(cur.val, cur.key)
            if key < cur.key:
                # search left
                cur = cur.left
        
            elif key > cur.key:
                # search right
                cur = cur.right

        # previous entry in the tree with the same key
        if cur is not None and cur.key == key:
            cur.val = val
            return
        
        newNode = TreeNode(key, val)
        # cur is None, meaning that key does not exist yet
        if key < prev.key:
            prev.left = newNode
        
        else:
            prev.right = newNode
        
        return




    def get(self, key: int) -> int:
        
        if self.root is None:
            return -1

        cur = self.root
        
        while cur is not None:
            
            if cur.key == key:
                return cur.val

            elif key < cur.key:
                cur = cur.left
            
            else:
                cur = cur.right
        
        return -1



    def getMin(self) -> int:
        if self.root is None:
            return -1

        cur = self.root
        while cur.left is not None:
            cur = cur.left
            
        return cur.val


    def getMax(self) -> int:
        if self.root is None:
            return -1
        
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node: TreeNode, key: int) -> TreeNode:
        if not node:
            return None
    
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right # no left child
            if not node.right:
                return node.left # no right child

            # two children: get inorder successor
            succ = self._find_min(node.right)
            node.key = succ.key
            node.val = succ.val
            node.right = self._remove(node.right, succ.key)
        return node


    def _find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        # dfs
        ino = []
        def helper(node, ino):


            if node is None:
                return
            
            helper(node.left, ino)
            ino.append(node.key)
            helper(node.right, ino)
        helper(self.root, ino)
        return ino


