length = float(input('Xin vui lòng nhập chiều dài: '))
breadth = float(input('Xin vui lòng nhập chiều rộng: '))
choose = input('Xin vui lòng chọn đơn vị: m , cm , dm  : ')

area = length * breadth 
if choose == 'm' :
    print(f'Diện tích hình chữ nhật là: {area} m2')
elif choose == 'cm' :
    print(f'Diện tích hình chữ nhật là: {area} cm2')
else :
    print(f'Diện tích hình chữ nhật là: {area} dm2')




