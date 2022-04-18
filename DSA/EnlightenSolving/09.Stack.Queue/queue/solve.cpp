#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define MAX 100000
using namespace std;

class Queue {
private:
  int que[MAX];
  int tail = 0, head = 0;

public:
  Queue() {}

  bool is_empty() {
    return head == tail;
  }

  bool is_full() {
    return head == (tail + 1) % MAX;
  }

  void enqueue(int x) {
    if (this->is_full()) {
      return;
    }

    que[tail] = x;
    tail++;
    if (tail == MAX) tail = 0;
  }

  int dequeue() {
    if (this->is_empty()) {
      return -1;
    }

    int res = que[head];
    ++head;
    if (head == MAX) head = 0;
    return res;
  }
};

auto print = [](auto x) {
  cout << x << '\n';
};

int main() {
  FastIO;

  Queue que;
  que.enqueue(10);
  que.enqueue(5);
  que.enqueue(3);
  que.enqueue(1);

  print(que.dequeue());
  print(que.dequeue());
  print(que.dequeue());
}
