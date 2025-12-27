chieu_cao = int(input('Nhập chiều cao tam giác: '))
for i in range(chieu_cao):
    for j in range(chieu_cao - i - 1):
      print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()