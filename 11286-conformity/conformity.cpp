#include <bits/stdc++.h>

using namespace std;

void solve(int n)   {
    map<vector<int>, int> mp;
    int higher = 0;
    while (n--) {
        vector<int> v(5);
        for (int i = 0; i < 5; i++) {
            cin >> v[i];
        }
        sort(v.begin(), v.end());
        higher = max(higher, ++mp[v]);
    }
    int ans = 0;
    for (auto m : mp)  {
        if (m.second == higher) {
            ans += higher;
        }
    }
    cout << ans << endl;
}

int main()  {
    int n;
    while (true)    {
        cin >> n;
        if (n == 0) {
            break;
        }
        solve(n);
    }
    return 0;
}