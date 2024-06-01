class Solution:
    def duplicates(self, arr, n): 
        element = {}
        duplicate = []
        
        # Count the frequency of each element in the array
        for i in arr:
            if i in element:
                element[i] += 1
            else:
                element[i] = 1
        
        # Identify elements that occur more than once
        for i, count in element.items():
            if count > 1:
                duplicate.append(i)
        
        # Return the sorted list of duplicates, or [-1] if no duplicates
        if not duplicate:
            return [-1]
        else:
            return sorted(duplicate)
    	    
solution = Solution()

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends