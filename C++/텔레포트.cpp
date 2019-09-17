#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;
int n, t, m;
bool sp[1000][1000];
bool check[1000];
int xs[1000];
int ys[1000];
int d[1000][1000];

int go(int i, int j) {
	int sx = xs[i], sy = ys[i];
	int dx = xs[j], dy = ys[j];
	if (sp[sx][sy] and sp[dx][dy]) {
		int temp = abs(sx - dx) + abs(sy - dy);
		if (temp < t) return temp;
		else return t;
	}
	if (d[i][j] != -1) {
		return d[i][j];
	}
	//cout << i << " " << j << "---------------" << endl;
	int answer = abs(sx - dx) + abs(sy - dy);
	for (int k = 0; k < n; k++) {
		if (!check[k]) {
			check[k] = true;
			//cout << i << " " << k << " " << j << endl;
			int temp = go(i, k) + go(k, j);
			if (answer > temp) {
				answer = temp;
			}
			check[k] = false;
		}
	}
	//cout << i << " " << j << " : " << answer << endl;
	bool ok = true;
	for (int k = 0; k < n; k++) {
		if (check[k] and (k != i and k != j)) {
			ok = false;
			break;
		}
	}
	if (ok) {
		d[i][j] = answer;
		d[j][i] = answer;
	}
	return answer;
}

int main() {
	memset(sp, false, sizeof(sp));
	memset(check, false, sizeof(check));
	memset(d, -1, sizeof(d));
	cin >> n >> t;
	for (int i = 0; i < n; i++) {
		int s, x, y;
		cin >> s >> x >> y;
		if (s) {
			sp[x][y] = true;
		}
		xs[i] = x, ys[i] = y;
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int src, dst;
		cin >> src >> dst;
		check[src - 1] = true;
		check[dst - 1] = true;
		cout << go(src - 1, dst - 1) << endl;
		check[src - 1] = false;
		check[dst - 1] = false;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			//cout << d[i][j] << " ";
		}
		//cout << endl;
	}
}