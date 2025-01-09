n=16
c=1
cnt=0
while c<=n:
    if n%c==0:
        print(f"factors of {n} is {c}")
        cnt+=1
    c+=1
if cnt==2:
    print("It is a prime number")
else:
    print("it is non-prime number")
print(f"count {cnt}")