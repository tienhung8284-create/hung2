'''
Chương trình làm tròn số
Tác giả: Trương Tiến Hùng
'''
import math
sotien = 63.333333

print(f'Số tiền được làm tròn là: ${round(sotien,2)}')
print(f'Số tiền được làm tròn là: ${round(sotien)}')

print(f'Số tiền được làm tròn là: ${math.ceil(sotien)}')
print(f'Số tiền được làm tròn là: ${math.floor(sotien)}')