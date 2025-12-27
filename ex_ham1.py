# Bước 1: Định nghĩa hàm

def add(num1,num2):
    return num1 + num2

# Bước 2: Gọi hàm
sum = add(5,10)     # Hàm chạy xong sẽ trả về kết quả, sau đó gán vào biến sum

print('Tổng:',sum)

sum1 = add(10,20)
print('Tổng:',sum1)

def info():
    print('My name is Teo')

info()

def printinfo(name):
    return name
print(printinfo('Hello Python'))