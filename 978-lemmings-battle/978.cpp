#include <bits/stdc++.h>

using namespace std;

void solve()    {
    multiset<int, greater<int>> green, blue;
    int x, b, sg, sb;
    cin >> b >> sg >> sb;
    for (int i = 0; i < sg; i++)    {
        cin >> x;
        green.insert(x);
    }
    for (int i = 0; i < sb; i++)    {
        cin >> x;
        blue.insert(x);
    }
    while (!green.empty() && !blue.empty())    {    
        auto itg = green.begin();
        auto itb = blue.begin();
        multiset<int, greater<int>> green_survivors, blue_survivors;
        for (int i = 0; i < b; i++) {
            if (itg == green.end() || itb == blue.end())    {
                break;
            }
            if (*itg > *itb)   {
                green_survivors.insert(*itg - *itb);
            }
            else if (*itg < *itb)   {
                blue_survivors.insert(*itb - *itg);
            }
            itg = green.erase(itg);
            itb = blue.erase(itb);
        }
        for (auto g : green_survivors)  {
            green.insert(g);
        }
        for (auto b : blue_survivors)   {
            blue.insert(b);
        }
    }
    if (green.empty() && blue.empty())  {
        cout << "green and blue died\n";
    }
    else if (blue.empty())  {
        cout << "green wins\n";
        for (auto g : green)    {
            cout << g << endl;
        }
    }
    else if (green.empty()) {
        cout << "blue wins\n";
        for (auto b : blue) {
            cout << b << endl;
        }
    }
}

int main()  {
    int n;

    cin >> n;
    while (n--) {
        solve();
        if (n > 0)  {
            cout << endl;
        }
    }
    return 0;
}