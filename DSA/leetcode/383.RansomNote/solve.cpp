#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    map<char, int> mp_ransom, mp_magazine;

    for (char ch : ransomNote) {
      if (mp_ransom.find(ch) == mp_ransom.end()) {
        mp_ransom[ch] = 0;
      }
      mp_ransom[ch]++;
    }

    for (char ch : magazine) {
      if (mp_magazine.find(ch) == mp_magazine.end()) {
        mp_magazine[ch] = 0;
      }
      mp_magazine[ch]++;
    }

    // check
    for (auto key : ransomNote) {
      char ch = key;
      char num = mp_ransom[key];

      if (mp_magazine.find(ch) == mp_magazine.end()) {
        return false;
      } else {
        if (mp_magazine[ch] < num) {
          return false;
        }
      }
    }
    return true;
  }
};

int main() {
  FastIO;
  auto sol = Solution();
  cout << (true == sol.canConstruct("a", "b")) << '\n';
  cout << (true == sol.canConstruct("aa", "ab")) << '\n';
  cout << (true == sol.canConstruct("aa", "aab")) << '\n';
  cout << (true == sol.canConstruct("aab", "baa")) << '\n';
}
