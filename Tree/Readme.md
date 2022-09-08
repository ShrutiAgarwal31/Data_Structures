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
  2. Complete Binary Tree - All the level except the last level is filled(i.e has 2 nodes). For the last level, it can be completely filled or fill from left to right. 
  3. Perfect Binary Tree - all the internal nodes have 2 children and all the leaf nodes are present in the same level.  
  4. Balanced Binary Tree - 
  5. Pathological Binary Tree - 
  
  ![image](https://user-images.githubusercontent.com/78465546/189138318-cd2d3fec-4da9-420b-a263-96ea67886396.png)
  
  ![image](https://user-images.githubusercontent.com/78465546/189138597-85e6b57d-c3a7-4cc9-b7cc-2c0d6df0cb59.png)
  
  ![image](https://user-images.githubusercontent.com/78465546/189141364-fdecf053-2ce7-4a01-9090-6e4dd27deb79.png)

  
Charecteristics:
  1. If tree have N nodes =>Number of Edges = (N-1)
  2. Every child has one Parent, but a Parent can have multiple child.
  3. Tress contain trees within them. i.e they are recursive.


  
