while True:
    try:
        num = int(input('Please enter a number: '))
    except:
        print('Sorry, please enter integer number')
    else:
        print(num)
        break
