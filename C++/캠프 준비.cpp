#include<vector>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;


vector<int> v;
vector<int> a;
int n, l, r, x;
int answer = 0;

void dfs(int idx) {
	if (idx == n) {
		if (v.size() < 2) return;
		else {
			int sum = 0;
			for (int i = 0; i < v.size(); i++) {
				sum += a[v[i]];
			}
			if (l <= sum && sum <= r && (a[v[v.size() - 1]] - a[v[0]]) >= x) {
				answer++;
			}
		}
	}
	else {
		dfs(idx + 1);
		v.push_back(idx);
		dfs(idx + 1);
		v.pop_back();
	}
}
int main() {
	cin >> n >> l >> r >> x;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		a.push_back(temp);
	}
	sort(a.begin(), a.end());
	dfs(0);
	cout << answer;
}