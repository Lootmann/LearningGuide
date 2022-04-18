#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define MAX 100000
using namespace std;

class Stack {
private:
  int st[MAX];
  int top = 0;

public:
  Stack() {}

  bool isEmpty() {
    return top == 0;
  }

  bool isFull() {
    return top == MAX;
  }

  void push(int x) {
    if (this->isFull()) {
      return;
    }

    st[top] = x;
    ++top;
  }

  int pop() {
    if (this->isEmpty()) {
      return -1;
    }

    --top;
    return st[top];
  }
};

int main() {
  FastIO;

  Stack st;

  st.push(3);
  st.push(5);
  st.push(7);

  cout << st.pop() << '\n';
  cout << st.pop() << '\n';

  st.push(9);
  cout << st.pop() << '\n';
}
