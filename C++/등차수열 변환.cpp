#include<iostream>
#include<vector>
using namespace std;

vector<int> b;
int n, answer = 100000;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		b.push_back(temp);
	}
	if (n == 1) {
		cout << 0;
		return 0;
	}
	for (int i = b[0] - 1; i <= b[0] + 1; i++) {
		for (int j = b[1] - 1; j <= b[1] + 1; j++) {
			int d = j - i;
			int temp = 0;
			if (i != b[0]) temp++;
			if (j != b[1]) temp++;
			int k;
			for (k = 2; k < n; k++) {
				if (b[k] - 1 <= i + k * d and i + k * d <= b[k] + 1) {
					if (b[k] != i + k * d) temp++;
				}
				else break;
			}
			if (k == n and answer > temp) answer = temp;
		}
	}
	if (answer == 100000) answer = -1;
	cout << answer;
}