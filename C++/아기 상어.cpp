#include<iostream>
#include<cstring>
#include<tuple>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int d[20][20];
bool check[20][20];
auto pos = make_tuple(0, 0);
vector<tuple<int, int>> v;	// 그턴에 후보 물고기들
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };

bool compare(tuple<int, int> a, tuple<int, int> b) {
	if (get<0>(a) != get<0>(b)) {
		return get<0>(a) < get<0>(b);
	}
	else {
		return get<1>(a) < get<1>(b);
	}
}

int main() {
	int n;
	cin >> n;
	for (int i= 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int temp;
			cin >> temp;
			if (temp == 9) {
				pos = make_tuple(i, j);
				temp = -1;
			}
			d[i][j] = temp;
			
		}
	}
	int size = 2, cnt = 0, time = 0;
	while (1) {
		memset(check, false, sizeof(check));
		queue<tuple<int, int, int>> q;
		int y, x;
		tie(y, x) = pos;
		q.push(make_tuple(y, x, 0));
		check[y][x] = true;
		int limit = 999999999;
		while (!q.empty()) {
			int y, x, t;
			tie(y, x, t) = q.front();
			q.pop();
			if (limit == 999999999 && 0 < d[y][x] && d[y][x] < size && d[y][x] != -1) {
				limit = t;
				v.push_back(make_tuple(y, x));
			}
			else if (limit == t && 0 < d[y][x] && d[y][x] < size && d[y][x] != -1) {
				v.push_back(make_tuple(y, x));
			}
			else if (t > limit) {
				continue;
			}
			else {
				for (int k = 0; k < 4; k++) {
					int ny = y + dy[k];
					int nx = x + dx[k];
					if (0 <= ny && ny < n && 0 <= nx && nx < n && !check[ny][nx] && d[ny][nx] <= size) {
						check[ny][nx] = true;
						if (t+1 <= limit) q.push(make_tuple(ny, nx, t + 1));
					}
				}
			}
			
		}
		if (v.empty()) {
			cout << time;
			return 0;
		}
		else {
			sort(v.begin(), v.end(), compare);
			d[get<0>(pos)][get<1>(pos)] = 0;
			d[get<0>(v[0])][get<1>(v[0])] = -1;
			pos = make_tuple(get<0>(v[0]), get<1>(v[0]));
			cnt++;
			time += limit;
			limit = 999999999;
			v.clear();
			if (size == cnt) {
				size++;
				cnt = 0;
			}
		}
	}
}
