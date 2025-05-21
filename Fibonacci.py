index = int(input("Nhap n: "))

if index==1 or index==2:
    print(1)
else:
    fibo = [1,1]
    for i in range(2,index+2):
        fibo.append(fibo[i-2]+fibo[i-1])
    for num in fibo[2:]:
        print(num, end=" ")
