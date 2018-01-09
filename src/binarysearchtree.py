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
    
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if(start):
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
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
        
        


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

print tree.findMin()
print tree.findMax()
print tree.height()
