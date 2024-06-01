class Solution:
    def oddEven(self, s):
        x = 0
        y = 0
        
        freq = {}
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1
            
            if position % 2 == 0 and count % 2 == 0:
                x += 1
            elif position % 2 != 0 and count % 2 != 0:
                y += 1
        
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"

solution = Solution()
    
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends