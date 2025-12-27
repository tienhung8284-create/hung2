import time
row = 5
for i in range(1,row+1,1):
    for j in range(1,row+1,1):
        print(j,end='')
        time.sleep(0.1)
    print('')

for i in range(1,row+1,1):
    for j in range(1,row+1,1):
        print('*',end=' ')
        time.sleep(0.1)
    print('')