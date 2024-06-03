
class Solution:
    def minDist(self, arr, n, x, y):
        last_pos_x = -1
        last_pos_y = -1
        min_distance = float('inf')
        
        for i in range(n):
            if arr[i] == x:
                last_pos_x = i
                if last_pos_y != -1:
                    min_distance = min(min_distance, abs(last_pos_x - last_pos_y))
            elif arr[i] == y:
                last_pos_y = i
                if last_pos_x != -1:
                    min_distance = min(min_distance, abs(last_pos_y - last_pos_x))
        
        if last_pos_x == -1 or last_pos_y == -1:
            return -1
        
        return min_distance

solution = Solution()
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends