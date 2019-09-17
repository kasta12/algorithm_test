#include<iostream>
#include<cmath>

using namespace std;
int n, t, m;
bool sp[1000];
int xs[1000];
int ys[1000];

int main() {
	cin >> n >> t;
	for (int i = 0; i < n; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a == 1) sp[i] = true;
		xs[i] = b, ys[i] = c;
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int s, d, answer;
		cin >> s >> d;
		answer = abs(xs[s - 1] - xs[d - 1]) + abs(ys[s - 1] - ys[d - 1]);
		/*if (!sp[s - 1] and !sp[d - 1]) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < n; k++) {
					if (j >= k) continue;
					if (!sp[j] or !sp[k]) continue;
					int a = abs(xs[s - 1] - xs[j]) + abs(ys[s - 1] - ys[j]) + abs(xs[d - 1] - xs[k]) + abs(ys[d - 1] - ys[k]);
					int b = abs(xs[s - 1] - xs[k]) + abs(ys[s - 1] - ys[k]) + abs(xs[d - 1] - xs[j]) + abs(ys[d - 1] - ys[j]);
					int val = a < b ? a : b;
					if (val + t < answer) answer = val + t;
				}
			}
		}
		else if (sp[s - 1] and !sp[d - 1]) {
			for (int j = 0; j < n; j++) {
				if (!sp[j]) continue;
				if (s - 1 == j) continue;
				int temp = abs(xs[d - 1] - xs[j]) + abs(ys[d - 1] - ys[j]) + t;
				if (temp < answer) answer = temp;
			}
		}
		else if (!sp[s - 1] and sp[d - 1]) {
			for (int j = 0; j < n; j++) {
				if (!sp[j]) continue;
				if (d - 1 == j) continue;
				int temp = abs(xs[s - 1] - xs[j]) + abs(ys[s - 1] - ys[j]) + t;
				if (temp < answer) answer = temp;
			}
		}
		else {
			if (t < answer) answer = t;
		}*/
		int a = 2000, b = 2000;
		for (int j = 0; j < n; j++) {
			if (sp[j]) {
				int temp;
				temp = abs(xs[s - 1] - xs[j]) + abs(ys[s - 1] - ys[j]);
				a = temp < a ? temp : a;
				temp = abs(xs[d - 1] - xs[j]) + abs(ys[d - 1] - ys[j]);
				b = temp < b ? temp : b;
			}
		}
		answer = a + b + t < answer ? a + b + t : answer;
		cout << answer << endl;
	}
}