'''
Viết chương trình cho phép người dùng nhập vào 2 số bất kỳ 
+ Tính tổng, hiệu, tích, thương, số dư, mũ
'''
def tinhtong(num1,num2):
    return num1 + num2
def tinhtich(num1,num2):
    return num1 * num2
def tinhhieu(num1,num2):
    return num1 - num2
def tinhthuong(num1,num2):
    return num1/num2
def tinhmu(num1,num2):
    return num1**num2
def tinhsodu(num1,num2):
    return num1 % num2

num1 = float(input('Nhập số thứ 1: '))
num2 = float(input('Nhập số thứ 2: '))

tong = tinhtong(num1,num2)
print('Tổng:',tong)

hieu = tinhhieu(num1,num2)
print('Hiệu:',hieu)

thuong = tinhthuong(num1,num2)
print('Thương:',thuong)

mu = tinhmu(num1,num2)
print('Mũ:',mu)

sodu = tinhsodu(num1,num2)
print('Số dư:',sodu)

tich = tinhtich(num1,num2)
print('Tích:',tich)