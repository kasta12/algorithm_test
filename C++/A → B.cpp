#include<iostream>
#include<queue>
#include<tuple>
using namespace std;
long long a, b;
int answer = -1;
queue<tuple<int, int>> q;
int main() {
	cin >> a >> b;
	q.push(make_tuple(a, 1));
	while (!q.empty()) {
		long long num;
		int t;
		tie(num, t) = q.front(); q.pop();
		if (num == b) {
			answer = t;
			break;
		}
		else {
			if (num * 2 <= b) q.push(make_tuple(num * 2, t + 1));
			if (num * 10 + 1 <= b) q.push(make_tuple(num * 10 + 1, t + 1));
		}
	}
	cout << answer;
}
// B->A로 생각하면 훨씬 쉽게 풀 수 있다. 생각해보자.