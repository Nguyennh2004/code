from time import time
t = time()
n,k = map(int, input().split())
    #lap n-1 lan
    #dem k-1 nguoi, duoi nguoi thu k
q = list(range(1,n+1))
print(q)
for i in range(1,n):
    for j in range(1,k):
        x = q.pop(0)
        q.append(x)
    q.pop(0)
    print(q)
print (q[0])
print( time() - t)
