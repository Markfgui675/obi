#include <bits/stdc++.h>

using namespace std;

int main(){
    int p, r;
    scanf("%d %d", &p, &r);
    if (p==0){
        cout << "C";
    } else if(p==1 && r==0){
        cout << "B";
    } else {
        cout << "A";
    }
}