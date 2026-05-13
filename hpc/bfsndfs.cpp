#include <iostream>
#include <queue>
#include <chrono>
#include <omp.h>

using namespace std;
using namespace chrono;

// Tree Node
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int value) {
        data = value;
        left = NULL;
        right = NULL;
    }
};

// Parallel BFS
void parallelBFS(Node* root) {

    if (root == NULL)
        return;

    queue<Node*> q;
    q.push(root);

    cout << "Parallel BFS Traversal: ";

    while (!q.empty()) {

        int size = q.size();

        Node* currentNodes[size];

        // Store current level nodes
        for (int i = 0; i < size; i++) {
            currentNodes[i] = q.front();
            q.pop();
        }

        // Process nodes in parallel
        #pragma omp parallel for
        for (int i = 0; i < size; i++) {

            Node* node = currentNodes[i];

            #pragma omp critical
            {
                cout << node->data << " ";
            }

            if (node->left) {

                #pragma omp critical
                {
                    q.push(node->left);
                }
            }

            if (node->right) {

                #pragma omp critical
                {
                    q.push(node->right);
                }
            }
        }
    }

    cout << endl;
}

// Parallel DFS
void parallelDFS(Node* root) {

    if (root == NULL)
        return;

    #pragma omp critical
    {
        cout << root->data << " ";
    }

    #pragma omp parallel sections
    {

        #pragma omp section
        {
            parallelDFS(root->left);
        }

        #pragma omp section
        {
            parallelDFS(root->right);
        }
    }
}

int main() {

    /*
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
    */

    Node* root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);

    root->left->left = new Node(4);
    root->left->right = new Node(5);

    root->right->left = new Node(6);
    root->right->right = new Node(7);

    // BFS Timing
    auto start1 = high_resolution_clock::now();

    parallelBFS(root);

    auto end1 = high_resolution_clock::now();

    auto duration1 =
    duration_cast<microseconds>(end1 - start1);

    cout << "BFS Execution Time: "
         << duration1.count()
         << " microseconds\n";

    // DFS Timing
    cout << "Parallel DFS Traversal: ";

    auto start2 = high_resolution_clock::now();

    parallelDFS(root);

    auto end2 = high_resolution_clock::now();

    auto duration2 =
    duration_cast<microseconds>(end2 - start2);

    cout << endl;

    cout << "DFS Execution Time: "
         << duration2.count()
         << " microseconds\n";

    return 0;
}
