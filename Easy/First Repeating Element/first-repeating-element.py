#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        element_data = {}
        
        for index in range(n):
            element = arr[index]
            if element in element_data:
                element_data[element]['count'] += 1
            else:
                element_data[element] = {'count': 1, 'first_index': index}
        
        min_index = float('inf')
        
        for element in element_data:
            if element_data[element]['count'] > 1:
                if element_data[element]['first_index'] < min_index:
                    min_index = element_data[element]['first_index']
        
        if min_index == float('inf'):
            return -1
        
        return min_index + 1

solution = Solution()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends