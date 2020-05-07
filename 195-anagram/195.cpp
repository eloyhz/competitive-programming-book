#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <cctype>

using namespace std;

bool comparator(char a, char b)
{
	char ta = tolower(a);
	char tb = tolower(b);

	if (ta == tb)	{
		return a < b;
	}
	return ta < tb;
}

int main()
{
	int n;
	string s;

	cin >> n;
	while (n-- > 0)	{
		cin >> s;
		sort(s.begin(), s.end(), comparator);
		do	{
			cout << s << endl;
		} while (next_permutation(s.begin(), s.end(), comparator));
	}
	return 0;
}

