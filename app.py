
n = int(input())
a = n
p = []
d = 2
count = 1
count_pow = []
count_save = 1
while d * d <= n:
    if n % d == 0:
        p.append(d)
        n //= d 
    else:
        d+=1
p.append(n)
p.append(a)
for i in range(len(p)-1):
    if p[i] == p[i+1]:
        count+=1   
    else :
        print(f'{p[i]} {count}')
        count = 1
        

    



