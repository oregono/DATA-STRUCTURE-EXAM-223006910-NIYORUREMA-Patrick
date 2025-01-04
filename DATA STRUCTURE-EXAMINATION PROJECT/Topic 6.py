class TreeNode:
    def __init__(self, event_name, tickets_available):
        self.event_name = event_name              
        self.tickets_available = tickets_available  
        self.left = None                          
        self.right = None                         


class BinaryTree:
    def __init__(self):
        self.root = None                          
        
    def add_event(self, event_name, tickets_available):
        """
        Add a new event to the binary tree.
        If the tree is empty, the event becomes the root.
        Otherwise, it is added to the correct position based on tickets available.
        """
        new_node = TreeNode(event_name, tickets_available)
        if self.root is None:                     
            self.root = new_node
            print(f"Added root event: {event_name}")
        else:                                     
            self._add(self.root, new_node)

    def _add(self, current, new_node):
        """
        Helper function to recursively add a new node to the correct position in the tree.
        """
        if new_node.tickets_available < current.tickets_available:
            if current.left is None:             
                current.left = new_node
                print(f"Added event {new_node.event_name} to the left of {current.event_name}")
            else:
                self._add(current.left, new_node)
        else:
            if current.right is None:            
                current.right = new_node
                print(f"Added event {new_node.event_name} to the right of {current.event_name}")
            else:
                self._add(current.right, new_node)

    def display_tree(self, node=None, prefix="", is_last=True):
        """
        Recursively displays the tree in a hierarchical format.
        """
        if node is None:
            node = self.root                      

        connector = "└── " if is_last else "├── "
        print(prefix + connector + f"{node.event_name} (Tickets: {node.tickets_available})")

        child_prefix = prefix + ("    " if is_last else "│   ")
        children = [node.left, node.right]
        children = [child for child in children if child is not None] 

        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            self.display_tree(child, child_prefix, is_last_child)

if __name__ == "__main__":
    bt = BinaryTree()

    bt.add_event("New Groove concert", 150)
    bt.add_event("Worship ceremony", 80)
    bt.add_event("RNB Buttle show", 200)
    bt.add_event("Come to jesus worship", 100)

    print("\nEvent Hierarchy:")
    bt.display_tree()
