while True:
    try: 
        age = float(input('Nhập tuổi: '))
    except:
        print('Xin vui lòng nhập lại tuổi.')
    else:
        try:
            if age > 130 :
                print('Tuổi không được quá 130.')
            if age < 0 :
                print('Tuổi không được nhập là số âm.')
        except:
            print('Nhập tuổi sai, xin vui lòng nhập lại tuổi.')
        else:
            if age > 18 and age < 130  :
                print('Người lớn')
                break
            elif age > 12 and age <= 18 :
                print('Thanh niên')
                break
            elif age > 5 and age <= 12 :
                print('Trẻ con')
                break
            elif age > 0 and age <= 5 :
                print('Em bé')
                break