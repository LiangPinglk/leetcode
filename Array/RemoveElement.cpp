#include <iostream>
using namespace std;
class Solution{
    public:
        int removeElement(int A[], int n, int elem){
            int i = 0;
            int j = 0;
            for(i = 0; i < n; i++){
                printf("%d\n",A[i]);
                if(A[i] == elem){
                    continue;
                }

                A[j] = A[i];
                j++;
            }
            return j;
        }
};
int main(){
    Solution solution;
    int A[7] = {1,2,3,4,5,6,4};
    int length = solution.removeElement(A,7,4);
    printf("%d\n",length);
};