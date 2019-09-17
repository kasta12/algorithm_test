#include<iostream>
using namespace std;
int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		int  maxVal = 0, sum = 0;
		for (int j = 0; j < n; j++) {
			int temp;
			cin >> temp;
			if (temp > maxVal) maxVal = temp;
			sum += temp;
		}
		cout << "#" << i + 1 << " " << sum + maxVal + n << endl;
	}
}