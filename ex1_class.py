# Định nghĩa class

class Cat:
    '''
    Đây là lớp con mèo
    - Tên: Tom
    - Tuổi: 5
    '''
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def Displayinfo(self):
        print('Tôi là',self.name)
        print('Tôi',self.age,'tuổi')
        print('Tôi màu',self.color)
    def Sleep(self):
        print(self.name,'đang ngủ')
    def Eat(self):
        print(self.name,'đang ăn')

class Dog:
    '''
    Đây là lớp con chó
    - Tên: Dollar
    - Tuổi: 6
    '''
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def Displayinfo(self):
        print('Tên tôi là',self.name)
        print('Tôi',self.age,'tuổi')
        print('Tôi màu',self.color)
    def Eat(self):
        print(self.name,'đang ăn')
    def Sleep(self):
        print(self.name,'đang ngủ')
      
class Mouse:
    '''
    Đây là lớp con chuột
    - Tên: Jery
    - Tuổi: 3
    '''
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def Displayinfo(self):
        print('Tên tôi là',self.name)
        print('Tôi',self.age,'tuổi')
        print('Tôi màu',self.color)
    def Eat(self):
        print(self.name,'đang ăn')
    def Sleep(self):
        print(self.name,'đang ngủ')

#print(Cat.__doc__)
#print(Dog.__doc__)
#print(Mouse.__doc__)

print(end='\n')

# Bước 2: Định nghĩa đối tượng 

ob_dog = Dog('Con chó 1',7,'đen')  # Tạo đối tượng con chó 1
ob_dog.Displayinfo()
ob_dog.Eat()
ob_dog.Sleep()

print('-'*30)

ob_mouse = Mouse('Con chuột 1',7,'đỏ')   # Tạo đối tượng con chuột 1
ob_mouse.Displayinfo()
ob_mouse.Eat()
ob_mouse.Sleep()

print('-'*30)

ob_cat = Cat('Con mèo 1',7,'cam')  # Tạo đối tượng con mèo 1
ob_cat.Displayinfo()
ob_cat.Eat()
ob_cat.Sleep()

print('-'*30)

ob_cat1 = Cat('Con mèo 2',7,'cam')
ob_cat1.Displayinfo()
ob_cat1.Eat()
ob_cat1.Sleep()

print('-'*30)

ob_cat2 = Cat('Con mèo 3',7,'cam')
ob_cat2.Displayinfo()
ob_cat2.Eat()
ob_cat2.Sleep()