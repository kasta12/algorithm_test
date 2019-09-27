#include<iostream>
#include<cmath>
using namespace std;
long long minVal(long long n) {
	return 2 * n + pow(3, n);
}
long long maxVal(long long n) {
	long long val = 1;
	for (long long i = 0; i < n; i++) {
		val *= 3;
		val += 2;
	}
	return val;
}
int func(long long cur, long long n3, long long n1, long long limit) {
	if (cur < 1) return 0;
	if (n3 == limit and n1 == 2 * limit) {
		if (cur == 1) return 1;
		else return 0;
	}
	else {
		int result = 0;
		if (n1 < 2 * limit) result += func(cur - 1, n3, n1 + 1, limit);
		if (n3 < limit and (n3 + 1) * 2 <= n1 and cur % 3 == 0) result += func(cur / 3, n3 + 1, n1, limit);
		return result;
	}
}
int solution(int n) {
	long long answer = 0;
	long long num = 1;
	while (true) {
		if (minVal(num) <= n and n <= maxVal(num)) {
			return func(n, 0, 0, num);
		}
		num++;
	}
}
int main() {
	cout << solution(2147483647);
}
