print('Division Calculator')
print('-'*30)

while True:
    try:
        num1 = float(input('Nhập số thứ 1: '))
        num2 = float(input('Nhập sô thứ 2: '))
    except ValueError:
        print('Nhập liệu sai, xin vui lòng nhập số')
    else:
        try:
            result = num1/num2    # Câu lệnh có thể xảy ra lỗi
        except ZeroDivisionError:
            print('Lỗi chia cho 0, mẫu số không được là 0')
        else:
            print(f'Kết quả: {result}')
            break