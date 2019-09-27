#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<tuple>
#include<string>
#include<algorithm>
#include<cstring>
#include<cmath>

using namespace std;

int n;
int num[20];
bool check[2500000];

void combination(int idx, int sum) {
	if (idx == n) {
		check[sum] = true;
	}
	else {
		combination(idx + 1, sum + num[idx]);
		combination(idx + 1, sum);
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) cin >> num[i];
	memset(check, false, sizeof(check));
	combination(0, 0);
	for (int i = 0; i < sizeof(check) / sizeof(bool); i++) {
		if (!check[i]) {
			cout << i;
			return 0;
		}
	}
}