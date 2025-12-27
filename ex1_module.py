from pkg.mod1 import load_data as bullet, load_data100 as gun
# Đi vào thư mục pkg, vào file mod1.py lấy hàm load_data()    

import pkg

print('Gun:',pkg.list_gun)
print('Bullet:',pkg.list_bullet)

bullet()  # load_data
gun()     # load_data100