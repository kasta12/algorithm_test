#include<iostream>
using namespace std;
int n, k;
int arr[1001];
int idx = 0, len = 0;

int main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int answer = 1000;
	for (int i = 0; i < n; i++) {
		if (arr[i] >= 1 + i * k) {
			int minVal = 0;
			for (int j = 0; j < n; j++) {
				if (arr[j] != arr[i] + k * (j - i)) {
					minVal++;
				}
			}
			if (minVal < answer) answer = minVal;
		}
	}
	cout << answer;
}
