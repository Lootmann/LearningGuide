#include <bits/stdc++.h>

#include <cstdio>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

struct Point {
  int x, y;
  Point(int x_ = -10001, int y_ = -10001) : x(x_), y(y_) {}
};

int dist(int x1, int y1, int x2, int y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void out(int x1, int y1, int x2, int y2) {
  printf("(%d, %d) (%d, %d)\n", x1, y1, x2, y2);
}

void solve() {
  int n;
  cin >> n;

  vector<Point> points(n);
  for (int i = 0; i < n; ++i) {
    int x, y;
    cin >> x >> y;
    points[i].x = x;
    points[i].y = y;
  }

  Point ans1, ans2;
  int max_dist = 10000 * 10000 + 1;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      int cur = dist(points[i].x, points[i].y, points[j].x, points[j].y);
      if (cur < max_dist) {
        max_dist = cur;

        ans1 = points[i];
        ans2 = points[j];
      }
    }
  }

  out(ans1.x, ans1.y, ans2.x, ans2.y);
  printf("dist = %d\n", max_dist);
}

int main() {
  FastIO;
  solve();
}
