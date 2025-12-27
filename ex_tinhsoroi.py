def ROI(doanhthu,chiphi):
    return (doanhthu-chiphi)/chiphi

def goiydautu(roi):
    if roi >=0.75:
        return 'Nên đầu tư'
    else:
        return 'Không nên đầu tư'

print('Chương trình tính ROI')
doanhthu=int(input('Nhập doanh thu: '))
chiphi=int(input('Nhập chi phí: '))
roi=ROI(doanhthu,chiphi)
print('Tỷ lệ ROI:',roi)
print('=>',goiydautu(roi))