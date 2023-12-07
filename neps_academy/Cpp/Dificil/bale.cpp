#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;

    scanf("%d", &n);

    int nums[n];
    int possiveis = 0;
    int i, j = 0;

    for (int i = 0; i < n; i++){
        scanf("%d", &nums[i]);
    }

    for(int i = 0; i<n; i++){
        for (int j = i+1; i<n; i++){
            if (nums[i] > nums[j]){
                possiveis++;
            }
        }
    }

    printf("%i", possiveis);
    return 0;


}
