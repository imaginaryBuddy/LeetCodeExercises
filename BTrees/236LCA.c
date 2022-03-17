/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode *left = NULL; 
    struct TreeNode *right = NULL; 
    if (root == NULL) return NULL; 
    else if (root->val == p->val || root->val == q->val) return root; 
    else {
        left = lowestCommonAncestor(root->left, p, q);
        right = lowestCommonAncestor(root->right, p, q);
    }
    if (left == NULL) return right; 
    if (right == NULL) return left;
    return root; 
} 
