//Checks if array is sorted in recursive manner 

int arraySort(int A[], int n){
    if(n == 1){
        return 1; 
    }
    return (A[n-1]<A[n-2])?0:arraySort(A, n - 1);
}