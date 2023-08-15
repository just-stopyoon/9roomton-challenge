#include <stdio.h>
int main() {
	int N, T, M, c; //필요한 기능의 개수
	scanf("%d", &N);
	scanf("%d %d", &T, &M); //현재시각 T시 M분
	int total = 0; //전체 걸리는 시간
	for (int i = 0 ; i < N ;i++){
		scanf("%d", &c); //i번째 기능을 개발하는데 걸리는 시간
		total += c;
	}
	T += total / 60;
	M += total % 60;
	T += M / 60;
	M %= 60;
	T = T % 24;
	printf("%d %d", T, M);
}