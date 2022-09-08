Tree Data Structure Concept:
  1. Non-Linear DS.
  2. Hierarchial Structure.
  3. Represenst relationships between nodes.

Terminology used:
  1. Nodes - Collection of entities. 
     Every node contains: value/data and/or link to the next node.
     Types of Nodes: 
      * Root Node - Top most node of the tree. Origin of tree DS.
      * Parent Node - It has an putgoing edge. Children are connected to it.  
      * Child Node - It has an incoming edge. Parent is connected to it. All nodes except the root node are the child nodes.
      * Leaf Node - No outgoing Edges. Has no children. Also called as External Node/Terminal Node.
      * Siblings - Nodes that belongs to the same Parent Node. They are at the same level.
      * Internal Node - Has atleast one child. All nodes except the leaf nodes.
  2. Edges/Link - Connection between the nodes.
  3. Degree -
      * Degree of a Node - Number of children that node has.
      * Degree of a Tree - Number of levels that tree contains.
  4. Level - 
  5. Height -
      * Height of a node - Total number of edges included in the Longest path from the leaf node to that node.
      * Height of a tree - Height of the root node.
  6. Depth - 
      * Depth of a node - Total number of edges from root node to that node.
        >> Depth of root node - 0
      * Depth of a Tree - Total number of edges from root to the last leaf node.

Types of Tree:
  1. General Tree - No limitation on the number of chil nodes.
  2. Binary Tree - At most 2 child nodes. (0, 1, 2) nodes are allowed.
  
Types of Binary Tree - 
  1. Full Binary Tree - Every node has either 0 or 2 children.
  2. Complete Binary Tree - 
  3. Perfect Binary Tree - 
  4. Balanced Binary Tree - 
  5. Pathological Binary Tree - 
  
  ![image](https://user-images.githubusercontent.com/78465546/189138136-7c28dc6d-a01f-4502-8951-3cdb4e3559c0.png)

  

Charecteristics:
  1. If tree have N nodes =>Number of Edges = (N-1)
  2. Every child has one Parent, but a Parent can have multiple child.
  3. Tress contain trees within them. i.e they are recursive.


  
