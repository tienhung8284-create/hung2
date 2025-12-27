
'''
Chương trình Python: In tên, tuổi, ngày sinh
Tác giả: Trương Tiến Hùng
Ngày phát hành: 23/06/2024
'''

# Khai báo biến
name = 'Hùng'
age = 15
dob = '26-December-2009' # Biến dob dùng để lưu ngày sinh

x = [1,2,3]              # Biến x là biến danh sách 


# Chương trình chính 
print(type(x))      #Hàm type() dùng để in kiểu dữ liệu của biến
print(x)            #In danh sách
print(type(name))
print(type(age))
print(type(dob))

print(name)
print(age)
print(dob)
print('Tên:',name,', Tuổi:',age,', Ngày sinh:',dob)
print(f'Tên: {name}, Tuổi: {age}, Ngày sinh: {dob}') # Dùng hàm f để in chuỗi và biến

class Animal:
    # Định nghĩa Class Animal
    pass

def Sum():
    #Hàm sum() dùng để tính tổng
    pass