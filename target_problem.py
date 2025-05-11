def sum1(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return True
        elif sum<target:
            left=left+1
        else:
            right=right+1
    return False
arr=[1,2,3,4,5]
target=7
result=sum1(arr,target)
print(result)
