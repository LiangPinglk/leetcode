#include <iostream>
class Solution{
public:
    int removeDuplicaes(int A[],int n){
        if(n == 0){
            return 0;
        }
        int j = 0;
        for(int i = 1; i < n; i++){
            if(A[j] != A[i]){
                A[++j] = A[i];
            }
        }
        return j + 1;
    }
};
int main(){
    Solution solution;
    int A[] = {1,1,2,2,3,3,6,6,7,8,9};
    int length = solution.removeDuplicaes(A, 11);
    printf("%d\n", length);
};