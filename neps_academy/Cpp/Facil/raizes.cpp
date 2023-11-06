#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<double> nums;
    int n;
    double x, r;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%lf", &x);
        r = sqrt(x);
        nums.push_back(r);
    }
    cout << fixed << setprecision(4);
    for (double k: nums){
        cout << k << endl;
    }
}
