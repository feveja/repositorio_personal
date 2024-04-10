#include <stdio.h>
#include <stdlib.h>

// Definición de la estructura del nodo del árbol
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

// Función para crear un nuevo nodo
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Función para insertar un nuevo nodo en el heap mínimo
void insertMinHeap(struct Node** root, int data) {
    if (*root == NULL) {
        *root = newNode(data);
        return;
    }
    if (data < (*root)->data) {
        int temp = (*root)->data;
        (*root)->data = data;
        data = temp;
    }
    if ((*root)->left == NULL)
        insertMinHeap(&((*root)->left), data);
    else if ((*root)->right == NULL)
        insertMinHeap(&((*root)->right), data);
    else if ((*root)->left->data < (*root)->right->data)
        insertMinHeap(&((*root)->left), data);
    else
        insertMinHeap(&((*root)->right), data);
}

// Función para insertar un nuevo nodo en el heap máximo
void insertMaxHeap(struct Node** root, int data) {
    if (*root == NULL) {
        *root = newNode(data);
        return;
    }
    if (data > (*root)->data) {
        int temp = (*root)->data;
        (*root)->data = data;
        data = temp;
    }
    if ((*root)->left == NULL)
        insertMaxHeap(&((*root)->left), data);
    else if ((*root)->right == NULL)
        insertMaxHeap(&((*root)->right), data);
    else if ((*root)->left->data > (*root)->right->data)
        insertMaxHeap(&((*root)->left), data);
    else
        insertMaxHeap(&((*root)->right), data);
}

// Función para imprimir el árbol de heap
void printHeap(struct Node* root) {
    if (root == NULL)
        return;
    printf("%d ", root->data);
    printHeap(root->left);
    printHeap(root->right);
}

int main() {
    struct Node* minHeap = NULL;
    struct Node* maxHeap = NULL;

    // Insertar elementos en el heap mínimo
    insertMinHeap(&minHeap, 3);
    insertMinHeap(&minHeap, 8);
    insertMinHeap(&minHeap, 1);
    insertMinHeap(&minHeap, 4);
    insertMinHeap(&minHeap, 6);
    printf("Min Heap: ");
    printHeap(minHeap);
    printf("\n");

    // Insertar elementos en el heap máximo
    insertMaxHeap(&maxHeap, 3);
    insertMaxHeap(&maxHeap, 8);
    insertMaxHeap(&maxHeap, 1);
    insertMaxHeap(&maxHeap, 4);
    insertMaxHeap(&maxHeap, 6);
    printf("Max Heap: ");
    printHeap(maxHeap);
    printf("\n");

    return 0;
}
