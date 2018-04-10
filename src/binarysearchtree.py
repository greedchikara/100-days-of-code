class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.preorder_insert(self.root, new_val)
    
    def preorder_insert(self, start, new_val):
        if start:
            if (new_val > start.value):
                if start.right:
                    self.preorder_insert(start.right, new_val)
                else:
                    start.right = Node(new_val)
            else:
                if start.left:
                    self.preorder_insert(start.left, new_val)
                else:
                    start.left = Node(new_val)
    def skew_insert(self, new_val):
        self.skew_preorder_insert(self.root, new_val)

    def skew_preorder_insert(self, start, new_val):
        if start:
            if (new_val > start.value):
                if start.left:
                    self.preorder_insert(start.left, new_val)
                else:
                    start.left = Node(new_val)
            else:
                if start.right:
                    self.preorder_insert(start.right, new_val)
                else:
                    start.right = Node(new_val)
                
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if(start):
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def print_inorder_tree(self):
        return self.inorder_print(self.root, '')[:-1]

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def print_postorder_tree(self):
        return self.postorder_print(self.root, '')[:-1]

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
    
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.preorder_search(start.right, find_val)
            else:
                return self.preorder_search(start.left, find_val)
        return False

    def findMin(self):
        return self.findMinRecursive(self.root);

    def findMinRecursive(self, start):
        while(start.left):
            start = start.left
        return start.value

    def findMinRecursiveNode(self, start):
        while(start.left):
            start = start.left
        return start

    def findMax(self):
        return self.findMaxRecursive(self.root)

    def findMaxRecursive(self, start):
        if not start.right:
            return start.value
        return self.findMaxRecursive(start.right)
        # while(start.right):
        #     start = start.right
        # return start.value

    def height(self):
        return self.findHeightRecursive(self.root)

    def findHeightRecursive(self, start):
        if not start:
            return -1
        return max(self.findHeightRecursive(start.left), self.findHeightRecursive(start.right)) + 1

    def printLevelOrderTraversal(self):
        queue = Queue(self.root)
        traversal = ""
        while len(queue.storage) > 0:
            node = queue.dequeue()
            traversal += (str(node.value) + "-")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal[:-1]
    
    def levelOrderTraversal(self, queue, traversal):
        node = queue.dequeue()
        if not node:
            return traversal
        traversal += ( str(node.value) + "-")
        queue.enqueue(node.left)
        queue.enqueue(node.right)
        self.levelOrderTraversal(queue, traversal)

    def isBST(self):
        return self.checkIfBST(self.root, float("-infinity"), float("infinity"))

    def checkIfBST(self, start, min_value, max_value):
        if start:
            if start.value > min_value and start.value < max_value and self.checkIfBST(start.left, min_value, start.value) and self.checkIfBST(start.right, start.value, max_value):
                return True
            else:
                return False
        return True

    def deleteNode(self, value):
        self.deleteFromTree(self.root, value)

    def deleteFromTree(self, start, value):
        if not start:
            return None

        if value < start.value:
            start.left = self.deleteFromTree(start.left, value)
        elif value > start.value:
            start.right = self.deleteFromTree(start.right, value)
        else:
            # Case 1: No Child
            if start.left == None and start.right == None:
                start = None
            # Case 2: One Child
            elif start.left == None:
                start = start.right
            elif start.right == None:
                start = start.left
            else:
                node = self.findMinRecursiveNode(start.right)
                start.value = node.value
                start.right = self.deleteFromTree(start.right, node.value)
            return start
            
                
            
    
class Queue(object):
    
    def __init__(self, head):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def dequeue(self):
        return self.storage.pop(0)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# tree.skew_insert(2)
# tree.skew_insert(1)
# tree.skew_insert(3)
# tree.skew_insert(5)

# print tree.print_tree()

# # Check search
# # Should be True
# print tree.search(4)
# # Should be False
# print tree.search(6)

# print tree.findMin()
# print tree.findMax()
# print tree.height()

# print tree.printLevelOrderTraversal()

print tree.print_inorder_tree()

# print tree.print_postorder_tree()

# print tree.isBST()

tree.deleteNode(2)
print tree.print_inorder_tree()
