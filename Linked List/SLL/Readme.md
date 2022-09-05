Single Linked Lists Data Structure:
  1. Each node is connectted to another link via a link.
  2. moves forward.
  3. moving in backward direction is not easy.

Operations:
  1. Adding elements --> break the existing link and add the node.
    Adding could be perform at the following positions:
    1. begin
      >> create a new node.
      >> point the next(newnode) to the first node of previously created SLL.
      >> change the head. point the head pointer to the new-node.
    2. end
      >> create a new node.
      >> traversing to the last node.
      >> point the next(last-node) to the new node that we created.
      >> point the next(new-node) to Null.
    3. in-between
      >> create a new-node.
      >> previous node - node before the new-node.
      >> next node - node after the new-node.
      >> point the next(previous node) to the new-node.
      >> point the next(new-node) to the next node.
    
  2. Removing Elements
    Deletion could be perform at the following positions:
    1. begin
      >> point the head to the second node(index 1).
    2. end
      >> traverse till the second-last node.
      >> point the nex(second-las) node to Null.
    3. in-between
      >> previous node - node before the deletion node.
      >> next node - node after the deletion node.
      >> point the nex(previous-node) to the next-node.
    
  3. Traversal
    1. Start with the head-node, if the head is not Null then access the info.
    2. Goto the next node to access the info.
    3. Repeat this process until the next(node) points to Null.
    
