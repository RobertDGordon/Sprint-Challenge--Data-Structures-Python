
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes 
        # for us to call `insert` on them 
        if value < self.value:
            # check if self.left is a valid node 
            if self.left:
                self.left.insert(value)
            # the left side is empty 
            else:
                # we've found a valid parking spot 
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        elif value == self.value:
            return value
        else:
            if self.right:
                self.right.insert(value)
            else:
                #add check for equal, return value:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #base case
        if self is None or self.value == target:
            return True
        if self.value < target and self.right:
            return self.right.contains(target)
        if self.value > target and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_v = self.value
        # next_node = self
        while self.right is not None:
            if self.right.value: #(type the order correctly lol)
                #If there is a right, check to make sure value is higher and then set
                if self.right.value > max_v:
                    max_v = self.right.value
            self = self.right
        return max_v

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def interative_for_each(self, cb):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current_node = stack.pop()

            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)