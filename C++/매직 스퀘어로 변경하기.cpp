#include<iostream>
#include<cmath>
#include<algorithm>

using namespace std;

int num[] = { 1,2,3,4,5,6,7,8,9 };
int s[3][3];
int answer = 100;
int main() {
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> s[i][j];
		}
	}
	do {
		if (num[0] + num[1] + num[2] != 15) continue;
		if (num[3] + num[4] + num[5] != 15) continue;
		if (num[6] + num[7] + num[8] != 15) continue;
		if (num[0] + num[3] + num[6] != 15) continue;
		if (num[1] + num[4] + num[7] != 15) continue;
		if (num[2] + num[5] + num[8] != 15) continue;
		if (num[0] + num[4] + num[8] != 15) continue;
		if (num[2] + num[4] + num[6] != 15) continue;
		int temp = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (s[i][j] != num[i * 3 + j]) {
					temp += abs(s[i][j] - num[i * 3 + j]);
				}
			}
		}
		if (temp < answer) {
			answer = temp;
		}
	} while (next_permutation(num, num + 9));
	cout << answer;
}