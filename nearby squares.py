t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_of_arr=0
    for i in arr:
        sum_of_arr+=i
    sum_of_arr=sum_of_arr

    def recursion(arr,i):
        if i>=len(arr):
            sum_of_b = sum(arr)
            sum_of_c = sum_of_arr - sum_of_b
            return abs(sum_of_b**2 - sum_of_c**2)
        sum_of_b=0
        for j in arr:
            sum_of_b+=j
        
        sum_of_c=sum_of_arr-sum_of_b
        ans=abs(sum_of_c**2-sum_of_b**2)


        srr=arr.copy()
        srr.pop(i)
        return min(ans,recursion(arr,i+1),recursion(srr,i))
    print(recursion(arr,0))
