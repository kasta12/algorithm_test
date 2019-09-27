#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
	string s = "ACFJMNRT";
	int answer = 0;
	do {
		int condition = 0;
		for (auto str : data) {
			int a, b;
			for (int i = 0; i < s.length(); i++) {
				if (s[i] == str[0]) a = i;
				if (s[i] == str[2]) b = i;
			}
			int cnt = max(a, b) - min(a, b) - 1;
			int val = stoi(str.substr(4, 1));
			if (str[3] == '=' && cnt == val) condition++;
			else if (str[3] == '<' && cnt < val) condition++;
			else if (str[3] == '>' && cnt > val) condition++;
			else break;
		}
		if (condition == data.size()) answer++;
	} while (next_permutation(s.begin(), s.end()));
	return answer;
}

int main() {
	int n = 2;
	vector<string> data;
	data.push_back("N~F=0");
	data.push_back("R~T>2");
}