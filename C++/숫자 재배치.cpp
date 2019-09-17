#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
string a;
int b, c, answer = -1;
int main() {
	cin >> a >> b;
	sort(a.begin(), a.end());
	do {
		c = stoi(a);
		if (a[0] == '0') continue;
		if (c <= b and answer < c) {
			answer = c;
		}
	} while (next_permutation(a.begin(), a.end()));
	cout << answer;
}