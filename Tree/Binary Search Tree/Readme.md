Binary Search Tree Concept: 
- Ordered data structure
- BST for child node values greater and less than the parent's values.
  1. Every node contains at most 2 childre, {0, 1, 2} child.
  2. left subtree of the node contains value lesser than the parent's value
  3. right subtree of the node contains value greater than the parent's value
  4. both left and right subtree must be a BST

- BST for duplicate keys
  * assumptions made in certain books: 
    1. duplicate values are not allowed in BST.
    2. if duplicate values are present then include it in the left node.
    3. if duplicate values are present then include it in the right node.
  

Operations:
  1. Insertion
  2. Deletion
  3. Traversal
    
    * In-Order
        1. traverse the left sub-tree
        2. visit the root node
        3. traverse the right sub-tree
    * Pre-Order  
        1. visit the root node
        2. traverse the left sub-tree
        3. traverse the right sub-tree
    * Post-Order
        1. traverse the left sub-tree
        2. traverse the right sub-tree
        3. visit the root node
    * Level-Order - all the nodes of a levels are accessed before jumping onto the next level 
  4. Searching
  
- Smallest node always occur in the left sub-tree i.e the leftmost node is the smallest value.
  * if the value of left sub-tree is null, then, parent node will be the smallest value
- Largest node always occur in the right sub-tree i.e the rightmost leaf node is the largest value.
  * if the value of right sub-tree is null, then, parent node will be the largest value
- Total number of nodes in BST: #nodes in left-sub-tree + #nodes in right-sub-tree + 1
