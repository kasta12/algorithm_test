#include<iostream>
#include<string>
using namespace std;
int main() {
	string s;
	cin >> s;
	int answer = 1;
	for (int i = 0; i < s.length(); i++) {
		if (i == 0) {
			if (s[i] == 'c') answer *= 26;
			else answer *= 10;
		}
		else {
			if (s[i] == 'c' and s[i - 1] == 'c') answer *= 25;
			else if (s[i] == 'd' and s[i - 1] == 'd') answer *= 9;
			else {
				if (s[i] == 'c') answer *= 26;
				else answer *= 10;
			}
		}
	}
	cout << answer;
}