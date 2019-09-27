#include <vector>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };

vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int numArea = 0, maxWidth = 0;
	bool check[100][100];
	memset(check, false, sizeof(check));
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (!check[i][j] and picture[i][j]) {
				numArea += 1;
				queue<tuple<int, int>> q;
				check[i][j] = true;
				q.push(make_tuple(i, j));
				int area = 0;
				int color = picture[i][j];
				while (!q.empty()) {
					int y, x;
					tie(y, x) = q.front(); q.pop();
					area += 1;
					for (int k = 0; k < 4; k++) {
						int ny = y + dy[k];
						int nx = x + dx[k];
						if (0 <= ny and ny < m and 0 <= nx and nx < n and !check[ny][nx] and picture[ny][nx] == color) {
							check[ny][nx] = true;
							q.push(make_tuple(ny, nx));
						}
					}
				}
				if (area > maxWidth) {
					maxWidth = area;
				}
			}
		}
	}
	vector<int> answer(2);
	answer[0] = numArea;
	answer[1] = maxWidth;
	return answer;
}