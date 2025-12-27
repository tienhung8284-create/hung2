from math import sqrt
print('Chuong trinh tinh dien tich tam giac')

while True:
    a = float(input('Nhap canh a > 0: '))
    b = float(input('Nhap canh b > 0: '))
    c = float(input('Nhap canh c > 0: '))

    if (a <= 0 or b <= 0 or c <= 0) or (a+b)<=c or (a+b)<=b or  (b+c)<=a:
        print('Tam giac khong hop le')
    else:
        cv=a+b+c
        p=cv/2
        dt=sqrt(p*(p-a)*(p-b)*(p-c))

        print('Dien tich tam giac la',dt)

    ans=input('Co muon lam tiep khong ?')
    if ans == 'k':
        break

print('Cam on ban da su dung chuong trinh.')