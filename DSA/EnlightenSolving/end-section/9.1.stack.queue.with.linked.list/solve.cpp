#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;
struct Node {
  int data;
  Node *next;
  Node(int d) : data(d) {}
};

class Stack {
private:
  Node *head;

public:
  Stack() {
    head = new Node(-1);
    head->next = head;
  }

  bool is_empty() {
    return head == head->next;
  }

  void push(int x) {
    Node *new_node = new Node(x);
    if (this->is_empty()) {
      head->next = new_node;
      new_node->next = head;
      return;
    }
    new_node->next = head->next;
    head->next = new_node;
  }

  int pop() {
    if (this->is_empty()) {
      return -1;
    }
    Node *old = head->next;
    head->next = head->next->next;
    return old->data;
  }

  void trace() {
    Node *cur = head->next;
    while (cur != head) {
      cout << cur->data << ' ';
      cur = cur->next;
    }
    cout << '\n';
  }
};

class Queue {
private:
  Node *head, *tail;

public:
  Queue() : head(nullptr), tail(nullptr) {}

  void enqueue(int n) {
    Node *new_node = new Node(n);
    if (this->is_empty()) {
      head = tail = new_node;
      return;
    }

    tail->next = new_node;
    tail = new_node;
  }

  int dequeue() {
    assert(!this->is_empty());

    int old = head->data;
    if (head == tail) {
      head = tail = nullptr;
      return old;
    }

    head = head->next;
    return old;
  }

  int front() {
    return head->data;
  }

  bool is_empty() {
    return head == nullptr && tail == nullptr;
  }
};

int main() {
  FastIO;

  cout << ">>> stack" << '\n';
  Stack st;
  for (int i = 0; i < 10; ++i) {
    st.push(i + 1);
  }

  while (!st.is_empty()) {
    cout << st.pop() << '\n';
  }

  cout << ">>> queue" << '\n';
  Queue que;
  for (int i = 0; i < 10; ++i) {
    que.enqueue(i + 1);
  }

  while (!que.is_empty()) {
    cerr << que.dequeue() << '\n';
  }
}
