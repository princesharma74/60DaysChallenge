#include<iostream>
using namespace std; 

int main(){
    int i, j, a[5][5];
    int savei, savej; 
    for(i = 0; i<5; i++){
        for(j = 0; j<5; j++){
            cin>>a[i][j]; 
            if (a[i][j]==1){
                savei = i+1; 
                savej = j+1; 
            }
        }
    }
    cout<<abs(3-savei) + abs(3 - savej); 
    return 0; 
}