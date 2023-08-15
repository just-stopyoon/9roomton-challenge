#include <stdio.h>
int main() {
	int W, R;
	scanf("%d %d", &W, &R);
	int RM = W * (1 + R / 30.0);
	printf("%d", RM);
	return 0;
}