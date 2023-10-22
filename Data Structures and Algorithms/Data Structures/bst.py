from collections import defaultdict


class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

        assert val is not None, "Cannot initialise a null node, just change the reference to None instead."
        
    def __repr__(self) -> str:
        return f"[Val: {self.val} left: {self.left} right: {self.right}]"

#   5
#  2  8
#       
    
class BST:
    def __init__(self, root) -> None:
        if not isinstance(root, Node):
            root = Node(root)

        self.root =  root
    
    def insert(self, val):
        def add_to_tree(val, node):
            if node is None:
                return Node(val)

            if val > node.val: node.right = add_to_tree(val, node.right)
            elif val <= node.val: node.left = add_to_tree(val, node.left)
            
            return node
            
        add_to_tree(val, self.root)
        
    def inorder(self):
        def traverse(node, lst):
            if node is None:
                return 

            traverse(node.left, lst)
            print(node)
            lst.append(str(node.val))
            traverse(node.right, lst)
            
        lst = []
        traverse(self.root, lst)
        return lst
       
    def level_order(self):
        def traverse(node, dict_, level):
            if node is None:
                return 

            traverse(node.left, dict_, level + 1)
            print(node)
            dict_[level].append(str(node.val))
            traverse(node.right, dict_, level + 1)
        
        dict_ = defaultdict(list)
        traverse(self.root, dict_, 0)
        
        print(dict(reversed(dict_.items())))

    @staticmethod
    def is_leaf(node):
        if node.left is None and node.right is None:
            return True
        
        return False
    
    def delete(self, val):
        
        def delete_node(node, val):
            if node is None:
                return node
            
            if node.val == val:
                if node.right is None:
                    temp = node.left
                    del node
                    return temp
                if node.left is None:
                    temp = node.right
                    del node
                    return temp
            
            if node < val:
                node.left = delete_node(node.left, val)
            elif node > val:
                node.right = delete_node(node.right, val)
                    

            return node
        
        
    def __repr__(self) -> str:
        return " ".join(self.inorder())




if __name__ == '__main__':
    bst = BST(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print(bst)
    bst.level_order() 
    
    
    #       50 
    #    /     \ 
    #   30      70 
    #  /  \    /  \ 
    # 20  40  60   80 
    
    
            