#include <vector>
using namespace std;

int MOD = 20170805;

int solution(int m, int n, vector<vector<int>> city_map) {
	int street[500][500][2];
	street[0][0][0] = 1;
	street[0][0][1] = 1;
	for (int i = 1; i < n; i++) {
		if (city_map[0][i] == 0) {
			street[0][i][0] = street[0][i - 1][1];
			street[0][i][1] = street[0][i - 1][1];
		}
		else if (city_map[0][i] == 1) {
			street[0][i][0] = 0;
			street[0][i][1] = 0;
		}
		else {
			street[0][i][0] = 0;
			street[0][i][1] = street[0][i - 1][1];
		}
	}
	for (int i = 1; i < m; i++) {
		if (city_map[i][0] == 0) {
			street[i][0][0] = street[i - 1][0][0];
			street[i][0][1] = street[i - 1][0][0];
		}
		else if (city_map[i][0] == 1) {
			street[i][0][0] = 0;
			street[i][0][1] = 0;
		}
		else {
			street[i][0][0] = street[i - 1][0][0];
			street[i][0][1] = 0;
		}
	}
	for (int y = 1; y < m; y++) {
		for (int x = 1; x < n; x++) {
			if (city_map[y][x] == 0) {
				street[y][x][0] = (street[y - 1][x][0] + street[y][x - 1][1]) % MOD;
				street[y][x][1] = (street[y - 1][x][0] + street[y][x - 1][1]) % MOD;
			}
			else if (city_map[y][x] == 1) {
				street[y][x][0] = 0;
				street[y][x][1] = 0;
			}
			else {
				street[y][x][0] = street[y - 1][x][0] % MOD;
				street[y][x][1] = street[y][x - 1][1] % MOD;
			}
		}
	}
	return street[m - 1][n - 1][0];
}