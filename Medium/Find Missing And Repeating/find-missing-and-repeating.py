#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        S = n * (n + 1) // 2
        P = n * (n + 1) * (2 * n + 1) // 6
        
        sum_arr = sum(arr)
        sum_squares_arr = sum(x * x for x in arr)
        
        diff_sum = S - sum_arr  # X - Y
        diff_squares = P - sum_squares_arr  # X^2 - Y^2
        
        sum_X_Y = diff_squares // diff_sum
        
        X = (diff_sum + sum_X_Y) // 2
        Y = X - diff_sum
        
        return [Y, X]

sol = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends