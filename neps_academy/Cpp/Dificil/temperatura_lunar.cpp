#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    vector<vector<int>> res;

    while (True){

        int n, m;
        cin >> n >> m;

        if (n == 0 && m == 0){
            break;
        }

        vector<int> temperaturas(n);
        for (int i = 0; i < n; ++i){
            cin >> temperaturas[i];
        }

        vector<int> medias;
        int i = m;
        int c = 0;

        while (i <= n){
            int soma = 0;
            for (int j = c; j < i; ++j){
                soma+=temperaturas[j];
            }
            medias.push_back(soma/m);
            i++;
            c++;
        }
        res.push_back({*min_element(medias.begin(), medias.end()), *max_element(medias.begin(), medias().end())});
    }

    for (size_t idx = 0; idx < res.size(); ++idx){
        cout << "Teste " << idx + 1 << endl;
        for (const auto& r : res[idx]){
            cout << r << " ";
        }
        cout << endl << endl;
    }

    return 0;

}
