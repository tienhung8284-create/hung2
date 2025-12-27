num = -30
print(num)

num1=3
num2=4

print(num1+num2)

a=-43.776
print(a)

print(5+6j)  # Số phức: 5 phần thực, 6 phần ảo
print(-2.1j) # Xuất phần ảo

print(5+6j.real)  # Xuất phần số thực
print((5+6j).imag)  # Xuất phần số ảo

a=True
print(a)
print(type(True))

print(isinstance(True,int))  # True là thể hiện của một đối tượng
print(isinstance('abc',str)) # Hàm isinstance lấy thể hiện của một đối tượng

p=10
q=True
r=9

print('*'*50)
print(p if q else r) # Nếu q là True thì in ra p ngược lại (nếu q là False) thì in r

print('*'*50)
p=True
q=False
print(p or q)
print(p and q)

print('*'*50)
print(not q)
print(not p)

print('*'*50)
q=[1,2,3,4,5]
p=3
print(p in q)  # in là phép toán thành viên (p có trong q hay không)

print('*'*50)
p=4
q=4
print(p is q)      # Kiểm tra p là q phải không.
print(p is not q)  # Kiểm tra p không phải q phải không.

print('*'*50)
# Thực hiện các toán tử so sánh
print(p > q)      # Kiểm tra p có lớn hơn q hay không.
print(p >= q)     # Kiểm tra p có lớn hơn hoặc bằng q hay không.
print(p < q)      # Kiểm tra p có nhỏ hơn q hay không.
print(p <= q)     # Kiểm tra p có nhỏ hơn hoặc bằng q hay không.
print(p == q)     # Kiểm tra p có bằng q hay không.
print(p != q)     # Kiểm tra p có khác q hay không.


# Thực hiện các toán tử Bitwise
# 2^7  2^6  2^5  2^4  2^3  2^2  2^1  2^0
# 128  64   32   16   8    4    2    1
# Số nhị phân biểu diễn bằng ký tự số 1 và 0
# Chuyển số thập phân thành số nhị phân
# Ví dụ:
# 0  0  0  0  0  1  0  1 => 5
# 0  0  0  0  0  0  1  1 => 3
p=5
q=3
#Bitwise OR     # 0 1 1 1 =>7
#Bitwise AND    # 0 0 0 1 => 1
#Bitwise XOR








