while True:
    try:
        mark = float(input('Nhập điểm: '))
    except:
        print(('Xin vui lòng nhập lại điểm'))
    else:
        try:
            if mark > 100 :
                print('Điểm không được quá 100')
            if mark < 0 :
                print('Điểm không được nhỏ hơn 0')
        except:
            print('Nhập điểm sai, vui lòng nhập lại điểm')
        else:
            if mark < 25 and mark >= 0 :
                print('F')
            if mark < 45 and mark >= 25 :
                print('E')
            if mark < 50 and mark >= 45 :
                print('D')
            if mark < 60 and mark >= 50 :
                print('C')
            if mark < 80 and mark >= 60 :
                print('B')
            if mark > 80 and mark <= 100:
                print('A')
            