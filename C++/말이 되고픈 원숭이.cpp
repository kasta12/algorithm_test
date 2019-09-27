#include<iostream>
#include<queue>
#include<tuple>
#include<cstring>

using namespace std;
int d[200][200];
int kk, w, h;
int dist[200][200][31];
int my[] = { 1,-1,0,0 };
int mx[] = { 0,0,1,-1 };
int hy[] = { -1,-2,-2,-1,1,2,2,1 };
int hx[] = { -2,-1,1,2,2,1,-1,-2 };

int main() {
	cin >> kk >> w >> h;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			cin >> d[i][j];
		}
	}
	memset(dist, -1, sizeof(dist));
	queue<tuple<int, int, int>> q;
	q.push(make_tuple(0, 0, 0));
	dist[0][0][0] = 0;
	while (!q.empty()) {
		int y, x, t, ny, nx;
		tie(y, x, t) = q.front(); q.pop();
		if (y == h - 1 && x == w - 1) break;
		for (int k = 0; k < 4; k++) {
			ny = y + my[k];
			nx = x + mx[k];
			if (0 <= ny && ny < h && 0 <= nx && nx < w && dist[ny][nx][t] == -1 && !d[ny][nx]) {
				dist[ny][nx][t] = dist[y][x][t] + 1;
				q.push(make_tuple(ny, nx, t));
			}
		}
		if (t < kk) {
			for (int k = 0; k < 8; k++) {
				ny = y + hy[k];
				nx = x + hx[k];
				if (0 <= ny && ny < h && 0 <= nx && nx < w && dist[ny][nx][t + 1] == -1 && !d[ny][nx]) {
					dist[ny][nx][t + 1] = dist[y][x][t] + 1;
					q.push(make_tuple(ny, nx, t + 1));
				}
			}
		}
	}
	for (int i = 0; i <= kk; i++) {
		if (dist[h - 1][w - 1][i] != -1) {
			cout << dist[h - 1][w - 1][i];
			return 0;
		}
	}
	cout << -1;
	return 0;
}