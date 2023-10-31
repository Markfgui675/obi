#include<bits/stdc++.h>

using namespace std;

int main(){
    int D;
    scanf("%d", &D);
    if (D<=800){
        printf("%d", 1);
    } else if (D>800 && D<=1400){
        printf("%d", 2);
    } else {
        printf("%d", 3);
    }
}
