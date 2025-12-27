from random import randrange

while True:
    computer_no = randrange(1,101)  # Số máy phát sinh ngẫu nhiên

    solandoan = 0
    flag_win = False

    while solandoan < 7:
        solandoan += 1

        person_no = int(input('Nhập một số: '))
        print('Bạn đã đoán lần thứ :',solandoan)

        if computer_no==person_no:
            print('Chúc mừng bạn đã đoán trúng.')
            flag_win=True
            break
        if computer_no > person_no:
            print('Ngu, Lớn hơn')
        if computer_no < person_no:
            print('Ngu, Nhỏ hơn')

    if flag_win == False:
        print('Game over! Số máy ra là:',computer_no)

    ans = input('Bạn có muốn chơi tiếp không?: ')
    if ans == 'k':
        break
print('Cút')