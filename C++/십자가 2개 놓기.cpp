#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
using namespace std;

vector<int> v;
int dy[] = { 1,-1,0,0 };
int dx[] = { 0,0,1,-1 };
int n, m;
char d[15][15];
bool check(int y, int x, int size) {
	for (int i = 0; i <= size; i++) {
		for (int k = 0; k < 4; k++) {
			int ny = y + i * dy[k], nx = x + i * dx[k];
			if (ny < 0 or ny >= n or nx < 0 or nx >= m) return false;
			if (d[ny][nx] != '#') return false;
		}
	}
	return true;
}
int answer = 1;

void dfs(int y, int x, int cnt) {
	if ((y == n - 1 and x == m - 1) or cnt == 2) {
		int result = 1;
		if (v.size() < 2) return;
		for (auto num : v) {
			result *= num;
		}
		answer = max(answer, result);
	}
	else if (x == m) {
		dfs(y + 1, 0, cnt);
	}
	else if (d[y][x] != '#') {
		dfs(y, x + 1, cnt);
	}
	else {
		for (int i = 0; i < 8; i++) {
			if (check(y, x, i)) {
				v.push_back(1 + i * 4);
				for (int j = 0; j <= i; j++) {
					for (int k = 0; k < 4; k++) {
						int ny = y + j * dy[k], nx = x + j * dx[k];
						d[ny][nx] = '-';
					}
				}
				dfs(y, x + i + 1, cnt + 1);
				v.pop_back();
				for (int j = 0; j <= i; j++) {
					for (int k = 0; k < 4; k++) {
						int ny = y + j * dy[k], nx = x + j * dx[k];
						d[ny][nx] = '#';
					}
				}
			}
		}
		dfs(y, x + 1, cnt);
	}
}
int main() {
	memset(d, '#', sizeof(d));
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		string temp;
		cin >> temp;
		for (int j = 0; j < m; j++) {
			if (temp[j] == '.') {
				d[i][j] = '.';
			}
		}
	}
	dfs(0, 0, 0);
	cout << answer;
}