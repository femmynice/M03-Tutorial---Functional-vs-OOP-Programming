def sort012(arr,N):
    low=mid=0
    high=N-1
    while mid <= high:
if arr[mid] == 0:
arr[low], arr[mid] = arr[mid], arr[low]
low += 1
mid += 1
elif arr[mid] == 1:
mid += 1
else:
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
arr[mid], arr[high] = arr[high], arr[mid]
high -= 1
...







#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# cdef binarysearch(arr, N, K):
low = 0
high = N - 1

while low <= high:
mid = (low + high) // 2

if arr[mid] == K:
return mid
elif arr[mid] < K:
low = mid + 1
else:
high = mid - 1

return -1ode here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends