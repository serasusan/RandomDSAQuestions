#include<bits/stdc++.h>

using namespace std;

int findMinMoves(string &word){
    int n = word.size();

    unordered_map<char,int> freq;
    
    for(int i=0;i<n;i++){
        freq[word[i]]+=1;
    }

    int moves = 0;
    // for(auto it=freq.begin();it!=freq.end();it++){
    for(auto it:freq){
        if(it.second>1){
            moves+=(it.second)/2;
        }
    }
    return moves;
}

int main(){
    return 0;
}