'''
Yêu cầu viết chương trình kiểm tra số âm, số dương và số 0
Gợi ý: Chỉ dùng cấu trúc if để kiểm tra
'''


print('Chương trình kiểm tra số âm, số dương và số 0')
print('-'*30)

while True:
    try:
        num1 = float(input('Nhập số: '))
        if num1 == 0:
            print('Số 0')
        if num1 > 0 :
            print('Số dương')
        if num1 < 0 :
            print('Số âm')
        break
    except:
        print('Nhập liệu sai, vui lòng nhập số')
