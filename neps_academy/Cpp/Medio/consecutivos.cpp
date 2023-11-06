#include<bits/stdc++.h>

using namespace std;

int main(){
    // Seu código vai aqui
	int n, x, anterior = 0, maiorSeq = 0, seq = 0;
	cin >> n;
	
	for (int i = 0; i < n; i++){
		cin >> x;
		if (i==0){
			seq++;
		} else {
			if(x==anterior){
				seq++;
			} else {
				if (seq > maiorSeq || i == n-1){
					maiorSeq = seq;
				}
				seq = 1;
			}
		}
		anterior = x;
	}
    printf("%d\n", maiorSeq);
	
    return 0;
}