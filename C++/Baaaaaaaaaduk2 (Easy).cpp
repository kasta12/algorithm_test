#include<iostream>
#include<queue>
#include<tuple>
#include<cstring>
using namespace std;

int d[20][20];
bool check[20][20];
int n, m;
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };
int bfs(int y, int x) {
	queue<tuple<int, int>> q;
	q.push(make_tuple(y, x));
	check[y][x] = true;
	int cnt = 1;
	bool ok = true;
	while (!q.empty()) {
		int y, x;
		tie(y, x) = q.front();
		q.pop();
		for (int k = 0; k < 4; k++) {
			int ny = y + dy[k];
			int nx = x + dx[k];
			if (0 <= ny && ny < n && 0 <= nx && nx < m) {
				if (d[ny][nx] == 2 && !check[ny][nx]) {
					check[ny][nx] = true;
					q.push(make_tuple(ny, nx));
					cnt++;
				}
				else if (d[ny][nx] == 0) {
					ok = false;
				}
			}
		}
	}
	if (ok) return cnt;
	else return 0;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> d[i][j];
		}
	}
	int answer = -1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (d[i][j] == 0) {
				d[i][j] = 1;
				for (int k = 0; k < n; k++) {
					for (int l = 0; l < m; l++) {
						if (i == k && j == l) continue;
						if (d[k][l] == 0) {
							d[k][l] = 1;
							int val = 0;
							memset(check, false, sizeof(check));
							for (int y = 0; y < n; y++) {
								for (int x = 0; x < m; x++) {
									if (d[y][x] == 2 && !check[y][x]) val += bfs(y, x);
								}
							}
							if (answer < val) answer = val;
							d[k][l] = 0;
						}
					}
				}
				d[i][j] = 0;
			}
		}
	}
	cout << answer;
}