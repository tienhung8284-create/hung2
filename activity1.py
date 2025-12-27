num1 = float(input('Xin vui lòng nhập số thứ 1: '))
num2 = float(input('Xin vui lòng nhập số thứ 2: '))
choose = input('Xin vui lòng chọn phép toán: +,-,*,/,//,%,**: ')

result = 0

if choose == '+' :
    result = num1 + num2 
elif choose == '-':
    result = num1 - num2
elif choose == '*' :
    result = num1 * num2
elif choose == '/' :
    result = num1 / num2
elif choose == '//' :
    result = num1 // num2
elif choose == '%' :
    result = num1 % num2
else:
    result = num1 ** num2

print(f'{num1} {choose} {num2} = {result}')