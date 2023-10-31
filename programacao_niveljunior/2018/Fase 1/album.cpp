#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, m, carta;
    scanf("%d", &n);
    scanf("%d", &m);
    vector<int> crts;
    int cs, flts = 0;
    for (int i = 0; i < m ; i++){
        scanf("%d", &carta);
        if (crts.size()==0){
            crts.push_back(carta);
        } else {
            cs = 0;
            for (int c: crts){
                if (c!=carta){
                    cs++;
                }
            }
            if (cs==crts.size()){
                crts.push_back(carta);
            }
        }
    }
    flts = n - crts.size();
    printf("%d", flts);
}
