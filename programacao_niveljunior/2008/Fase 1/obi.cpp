#include<bits/stdc++.h>

using namespace std;

int main(){
    int students;
    int min_pontuation;
    int aproved_students = 0;
    scanf("%d %d", &students, &min_pontuation);
    int ponto1;
    int ponto2;
    int soma = 0;
    for (int i = 0; i < students; i++){
        scanf("%d %d", &ponto1, &ponto2);
        soma = ponto1+ponto2;
        if (soma >= min_pontuation){
            aproved_students++;
        }
    }
    printf("%d",aproved_students);
    return 0;
}
