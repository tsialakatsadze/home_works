
# მოიძიეთ ინფორმაცია ბინარულ ხეზე და დაწერეთ დაბეჭდვის ფუნქცია printLeafNodes-თვის


        #                                          50
        #                  30                                              63
        #       15                      43                      59                      77    
        # 10          25          36          48          ##          ##          73          81


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert(current_node.left, value)
        
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert(current_node.right, value)
        else:
            return
    
    def show(self):
        result = []
        self._show(self.root,result)
        return result
    def _show(self, node, result):
        if node:
            self._show(node.left, result)
            result.append(node.value)
            self._show(node.right, result)
    
    def parent(self, value):
        parent_node = self._parent(None, self.root, value)
        if parent_node:
            return parent_node.value
        return
    def _parent(self, parent_att, node, value):
        if node is None:
            return None
        if node.value == value:
            return parent_att
        parent_left = self._parent(node, node.left, value)
        parent_right = self._parent(node, node.right, value)
        return parent_left or parent_right
    
    def children(self, value):
        node = self._children(self.root, value)
        if node:
            child_list =[]
            if node.left:
                child_list.append(node.left.value)
            if node.right:
                child_list.append(node.right.value)
            return child_list
        return
    def _children(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_child = self._children(node.left, value)
        right_child = self._children(node.right, value)
        return left_child or right_child

tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(63)
tree.insert(15)
tree.insert(43)
tree.insert(59)
tree.insert(77)
tree.insert(10)
tree.insert(25)
tree.insert(36)
tree.insert(48)
tree.insert(73)
tree.insert(81)

#                                                  50
#                          30                                              63
#               15                      43                      59                      77    
#         10          25          36          48          ##          ##          73          81

print(tree.show())       # [10, 15, 25, 30, 36, 43, 48, 50, 59, 63, 73, 77, 81]
print(tree.parent(73))   # 77
print(tree.parent(81))   # 77
print(tree.parent(43))   # 30
print(tree.children(50)) # [30, 63] 
print(tree.children(30)) # [15, 43] 
print(tree.children(63)) # [59, 77] 
print(tree.children(15)) # [10, 25] 
print(tree.children(43)) # [36, 48] 
print(tree.children(59)) # []       
print(tree.children(77)) # [73, 81] 
