// check whether two trees are the same or not 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if (p == NULL && q == NULL) return 1; 
    else if ((p == NULL && q != NULL )|| (p != NULL && q == NULL)) return 0 ; 
    else {
        if (p->val == q->val) return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right)); 
        else return 0; 
    }
}
