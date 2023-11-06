#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, b, c = 0;
    string cem = "";
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++){
        scanf("%d", &b);
        nums[i] = b;
    }
    for (int i = 0; i < n; i++){
        if (i%3==0 && i > 0){
            if (cem=="100"){
                c++;
            }
            cem = "";
        } else {
            cem+=to_string(nums[i]);
        }
    }
    cout << c;
    return 0;
}
