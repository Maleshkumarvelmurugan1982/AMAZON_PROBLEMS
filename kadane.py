n=int(input("Enter the size of the array:"))
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
current=arr[0]
maxs=arr[0]
for i in range(1,n):
    current=max(arr[i],arr[i]+current)
    if(current>maxs):
        maxs=current
print(maxs)
