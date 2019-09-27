#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
#include<queue>
#include<cstring>
#include<string>

using namespace std;

int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };
int d[1000][1000];
int dist[1000][1000][11];
int n, m, k;
int answer = 10000;

int main() {
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		string temp;
		cin >> temp;
		for (int j = 0; j < m; j++) {
			d[i][j] = stoi(temp.substr(j, 1));
		}
	}
	queue<tuple<int, int, int>> q;
	q.push(make_tuple(0, 0, 0));
	dist[0][0][0] = 1;
	while (!q.empty()) {
		int y, x, t;
		tie(y, x, t) = q.front(); q.pop();
		for (int z = 0; z < 4; z++) {
			int ny, nx;
			ny = y + dy[z];
			nx = x + dx[z];
			if (0 <= ny && ny < n && 0 <= nx && nx < m) {
				if (d[ny][nx] == 1 && t < k && dist[ny][nx][t + 1] == 0) {
					dist[ny][nx][t + 1] = dist[y][x][t] + 1;
					q.push(make_tuple(ny, nx, t + 1));
				}
				if (d[ny][nx] == 0 && dist[ny][nx][t] == 0) {
					dist[ny][nx][t] = dist[y][x][t] + 1;
					q.push(make_tuple(ny, nx, t));
				}
			}
		}
	}
	int ans = -1;
	for (int i = 0; i <= k; i++) {
		if (dist[n - 1][m - 1][i] == 0) continue;
		if (ans == -1) {
			ans = dist[n - 1][m - 1][i];
		}
		else if (ans > dist[n - 1][m - 1][i]) {
			ans = dist[n - 1][m - 1][i];
		}
	}
	cout << ans;
	return 0;
}