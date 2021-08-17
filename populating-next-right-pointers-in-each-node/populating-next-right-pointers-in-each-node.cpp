/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        // trying c++ for a change (never trying it again 😩)
        if (root == NULL) 
            return root;
        
        Node* previous = root;
        Node* current = NULL;
        while (previous) {
            current = previous;
            while (current && current->left) {
                // left next points to right
                current->left->next = current->right;
                if (current->next) {
                    // sets right next to next's left which might be NULL
                    current->right->next = current->next->left;
                }
                current = current->next;
            }
            previous = previous->left;
        }
        
        return root;
        
    }
};