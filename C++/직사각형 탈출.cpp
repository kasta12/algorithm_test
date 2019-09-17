#include<iostream>
#include<cstring>
#include<queue>
#include<tuple>
#include<vector>
using namespace std;
int dist[1000][1000];
int n, m, h, w, sr, sc, fr, fc;
int d[1000][1000];
queue<tuple<int, int>> q;
vector<tuple<int, int>> v;
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };
int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int temp;
			cin >> temp;
			if (temp == 1) {
				v.push_back(make_tuple(i, j));
			}
			d[i][j] = temp;
		}
	}
	cin >> h >> w >> sr >> sc >> fr >> fc;
	memset(dist, -1, sizeof(dist));
	q.push(make_tuple(sr - 1, sc - 1));
	dist[sr - 1][sc - 1] = 0;
	while (!q.empty()) {
		int y, x;
		tie(y, x) = q.front();
		q.pop();
		for (int k = 0; k < 4; k++) {
			int ny = y + dy[k], nx = x + dx[k];
			if (0 <= ny and ny < n and 0 <= nx and nx < m and dist[ny][nx] == -1) {
				if (ny + h - 1 < n and nx + w - 1 < m) {
					bool ok = true;
					for (int i = 0; i < v.size(); i++) {
						int vy, vx;
						tie(vy, vx) = v[i];
						if (ny <= vy and vy < ny + h and nx <= vx and vx < nx + w) {
							ok = false;
							break;
						}
					}
					if (ok) {
						dist[ny][nx] = dist[y][x] + 1;
						q.push(make_tuple(ny, nx));
					}
				}
			}
		}
	}
	cout << dist[fr - 1][fc - 1];
}