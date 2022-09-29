# Binary Trees Problems 

## 236. LCA 
Definitions: 
LCA = "the lowest common ancestor of two nodes v and w in a tree or directed acyclic graph T is the 
lowest node that has both v and w as descendants, where we define each node to be a descendant of itself." (Wikipedia)
Note: 
- p and q are guaranteed to be in the tree. 
Cases: 
![IMG_1404](https://user-images.githubusercontent.com/81760484/192912699-e36556f9-10e4-4405-825d-9fc233e57d51.jpg)

Case 1:  A is obviously the LCA. 
Case 1 extended: now, if A is the first node to have its left and right subtree have both p and q, then A is the LCA. 
Case 2: p/q is parent of q/p 

Approach: Use Recursion  
1. Base cases: 
  - if the node is null, then return null. In other words, we haven't found p or q yet. 
  - if the node.val == p OR node.val == q, then return the node. We have found it. 
2. We want the algorithm to return p or q, at each step of "moving back up the recursion tree", so that we can eventually find the node: 
![IMG_1405](https://user-images.githubusercontent.com/81760484/192914087-6e63671e-7d1e-457e-b0da-ea847680d671.jpg)

3. Therefore, we store the return value of each recursive call. 
  - `left = lowestCommonAncestor(root.left, p, q)`
  - `right = lowestCommonAncestor(root.right, p, q)`
4. If both left and right == null, then we haven't found any yet. 
5. If only left == null, there're two possibilities: 1. p/q parent of the other 2. we have only found one from that subtree, so keep searching. 
6. Similar for if only right == null. 
7. Thus, we can summarise the above: 
  - `if left == null, return right`
  - `if right == null, return left` 
  - note that: 4. is accounted for, because we will return null as right == null 
8. If we have both left and right, then current root is LCA.  
