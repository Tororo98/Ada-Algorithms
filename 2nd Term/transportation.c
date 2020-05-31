#include <stdio.h> 
#include <string.h> 
#include <stdlib.h>
int num[10];
struct {
	int x,y,nu;
} Node[30];

int m,cnt,max,n,sum;

void Solve (int t) {
	for (int i=t; i<m; i++) {
		int flag = 0;
		for (int k=node[i].x; k<node[i].y ; k++) {
			if (num[k]+node[i].nu > Sum) {
				flag = 1;
				break;
			}
		}
		if (flag = = 0) {
			for (int k=node[i].x; k<node[i].y; k++) {
				num[k]+=node[i].nu;
			}
			CNT + = (node[i].y-node[i].x) *node[i].nu;
			if (cnt > Max) max = Cnt;solve (i+1); 
			for (int k=node[i].x; k<node[i].y; k++) { 
				num[k]-=node[i].nu;
			}
			CNT-= (node[i].y-node[i].x) *node[i].nu;
		}
	} return;
}
int main () {
	int i;
	while (scanf ("%d%d%d", &sum,&n,&m), n| | m| | sum) {
		max = CNT = 0;
		memset (num,0,sizeof (num)), memset (node,0,sizeof (node)), for (i=0; i<m; i++) {
			scanf ("%d%d%d",& node[i].x,&node[i].y,&node[i].nu);
		} 
		Solve (0);p rintf ("%d\n", Max);
	}
}