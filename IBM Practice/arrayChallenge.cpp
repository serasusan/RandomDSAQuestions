#include<bits/stdc++.h>
using namespace std;

vector<long> arrayChallenge(vector<long> arr){
    vector<long> res;
    int n = arr.size();
    res.push_back(0);
    for(int i=1;i<n;i++){
        int sum = 0;
        for(int j=0;j<i;j++){
            sum+=arr[i]-arr[j];
        }
        res.push_back(sum);
    }
    return res;
}


int main(){
    vector<long> arr = {2,1,3};
    vector<long> res = arrayChallenge(arr);
    for(int i=0;i<res.size();i++){
        printf("%ld ", res[i]);
    }
    return 0;
}