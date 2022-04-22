#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

struct Heap {
  vector<int> heap;
  Heap() {}

  void push(int x) {
    heap.emplace_back(x);
    int i = (int)heap.size() - 1;

    while (i > 0) {
      int p = (i - 1) / 2;
      if (heap[p] > x) break;
      heap[i] = heap[p];
      i = p;
    }
    heap[i] = x;
  }

  int top() {
    if (!heap.empty())
      return heap[0];
    else
      return -1;
  }

  void pop() {
    if (heap.empty()) return;

    int x = heap.back();
    heap.pop_back();
    int i = 0;
    while (i * 2 + 1 < (int)heap.size()) {
      int child1 = i * 2 + 1, child2 = i * 2 + 2;
      if (child2 < (int)heap.size() && heap[child2] > heap[child1]) {
        child1 = child2;
      }

      if (heap[child1] <= x) break;
      heap[i] = heap[child1];
      i = child1;
    }
    heap[i] = x;
  }
};

int main() {
  FastIO;

  Heap heap;
  heap.push(5);
  heap.push(3);
  heap.push(7);
  heap.push(1);

  cout << heap.top() << endl;
  heap.pop();
  cout << heap.top() << endl;

  heap.push(11);
  cout << heap.top() << endl;
}
