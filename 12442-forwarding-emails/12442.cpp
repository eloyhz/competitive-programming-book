#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <algorithm>

using namespace std;

struct info {
    int from;
    int to;
    int distance;
    bool visited;
};

int bfs(vector<info>& data, int start)  {
    if (data[start].visited)    {
        return 0;
    }
    data[start].visited = true;
    int end = data[start].to;
    return bfs(data, end) + 1;
}

int main()
{
    int t, n, u, v, i, r, m;

    cin >> t;
    for (i = 0; i < t; i++)   {
        cin >> n;
        vector<info> mail(n + 1, info{-1, -1, 0, false});
        while (n-- > 0)  {
            cin >> u >> v;
            mail[u] = info{u, v, 0, false};
        }
        r = 0;
        for (auto& m : mail) {
            if (m.from == -1) {
                continue;
            }
            m.distance = bfs(mail, m.from);
            if (m.distance > r) {
                r = m.distance;
            }
            for (auto& d : mail)    {
                if (d.from == -1)   {
                    continue;
                }
                d.visited = false;
            }
        }
        set<int> w;
        for (auto& m : mail)    {
            if (m.from == -1)   {
                continue;
            }
            if (m.distance == r)    {
                w.insert(m.from);
            }
        }
        cout << "Case " << i + 1 << ": " << *min_element(w.begin(), w.end()) << endl;
    }
}