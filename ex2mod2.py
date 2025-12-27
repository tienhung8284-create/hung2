g = 5
def increment():
    global g
    g=2
    g+=1
increment()
print(g)