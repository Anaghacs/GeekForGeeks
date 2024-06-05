#User function Template for python3

class Solution:
    
    def binSort(self, A, N): 
        count0 = 0
        
        for i in range(N):
            if A[i] == 0:
                count0 += 1
        
        for i in range(count0):
            A[i] = 0
        for i in range(count0, N):
            A[i] = 1
    
solution = Solution()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends