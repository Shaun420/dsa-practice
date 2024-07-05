#include <iostream>

struct Node {
    int data;
    Node* next;
};

// Function to traverse and print the elements of the linked
// list
void traverseLinkedList(Node* head)
{
    // Start from the head of the linked list
    Node* current = head;

    // Traverse the linked list until reaching the end
    // (nullptr)
    while (current != nullptr) {
        // Print the data of the current node
        std::cout << current->data << " ";

        // Move to the next node
        current = current->next;
    }

    std::cout << std::endl;
}

// Example usage:
// Assuming the linked list is already constructed

int main()
{
    // Create nodes
    Node* head = new Node{ 1 };
    Node* second = new Node{ 2 };
    Node* third = new Node{ 3 };

    // Connect nodes
    head->next = second;
    second->next = third;

    // Call the traverseLinkedList function to print the
    // linked list elements
    traverseLinkedList(head);

    // Memory cleanup (free allocated memory)
    delete head;
    delete second;
    delete third;

    return 0;
}
