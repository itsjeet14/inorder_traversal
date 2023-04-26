# Python3 program for inorder traversal of a binary tree

# A class that represents an individual node in a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to perform inorder traversal
def inorderTraversal(root):
    if root:
        # Recur on the left subtree
        inorderTraversal(root.left)
        # Print the node value
        print(root.val, end=" ")
        # Recur on the right subtree
        inorderTraversal(root.right)

# Driver code
if __name__ == "__main__":
    # Get the tree input from the user
    arr = list(map(int, input("Enter the nodes of the binary tree: ").split()))
    
    # Construct the binary tree from the input array
    root = Node(arr[0])
    node_dict = {0: root}
    i = 1
    while i < len(arr):
        parent_index = (i-1)//2
        parent_node = node_dict[parent_index]
        if arr[i] != -1:
            left_node = Node(arr[i])
            parent_node.left = left_node
            node_dict[i] = left_node
        if i+1 < len(arr) and arr[i+1] != -1:
            right_node = Node(arr[i+1])
            parent_node.right = right_node
            node_dict[i+1] = right_node
        i += 2
    
    # Perform inorder traversal and print the output
    print("Inorder Traversal of the binary tree is: ")
    inorderTraversal(root)
