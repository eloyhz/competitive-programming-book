#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
	vector<tuple<int, int, int>> el;
	int w, iq, i, j;

	i = 1;
	while (cin >> w >> iq)	{
		el.push_back({iq, w, i++});
	}
	// Sort elephants by IQ in decreasing order
	sort(el.rbegin(), el.rend());

	/*
	for (auto a : el)	{
		cout << get<0>(a) << ", " << get<1>(a) << ", " << get<2>(a) << endl;
	}
	*/

	// LIS in increasing weight
	int LIS[el.size()], PRED[el.size()];

	for (i = 0; i < el.size(); i++)	{
		PRED[i] = -1;
		LIS[i] = 1;
		for (j = 0; j < i; j++)	{
			if (get<1>(el[j]) < get<1>(el[i]))	{
				if (LIS[j] + 1 > LIS[i])	{
					LIS[i] = LIS[j] + 1;
					PRED[i] = j;
				}
			}
		}
	}
	/*
	for (i = 0; i < el.size(); i++)	{
		cout << i << ": " << LIS[i] << ", " << PRED[i] << endl;
	}
	cout << "max = " << max_element(LIS, LIS + el.size()) - LIS << endl;
	*/
	int imax = max_element(LIS, LIS + el.size()) - LIS;
	int p = imax;
	stack<int> st;
	while (PRED[p] != -1)	{
		// cout << p << endl;
		st.push(p);
		p = PRED[p];
	}
	// cout << p << endl;
	st.push(p);

	cout << st.size() << endl;
	while(!st.empty())	{
		p = st.top();
		st.pop();
		cout << get<2>(el[p]) << endl;
	}
		
	return 0;
}
