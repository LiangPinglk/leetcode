#include <iostream>
#include <vector>
using namespace std;
class Solution{
    public:
    vector <vector<int> > generate(int numRows){
        vector<vector<int> > vals;
        vals.resize(numRows);
        for(int i = 0;i < numRows; i++){
            vals[i].resize(i+1);
            vals[i][0] = 1;
            vals[i][vals[i].size() - 1] = 1;
            for(int j = 1; j < vals[i].size() - 1; j++){
                vals[i][j] = vals[i - 1][j - 1] + vals[i - 1][j];
            }
        }
        return vals;
    }
};
int main(){
    Solution sol;
    vector <vector<int> > pascaTriangle;
    pascaTriangle = sol.generate(5);
    for (int i = 0; i<pascaTriangle.size(); i++){
        for (int j = 0; j < i+1; j++){
            printf("%d\t", pascaTriangle[i][j]);
        }
        printf("\n");
    }
};