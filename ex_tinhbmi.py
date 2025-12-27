def BMI(height,weight):
    return weight/(height**2)

def PhanLoai(bmi):
    if bmi<18.5:
        return 'Gầy'
    if bmi<=24.9:
        return 'Bình Thường'
    if bmi<=29.9:
        return 'Hơi béo'
    if bmi<=34.9:
        return 'Béo phì cấp độ 1'
    if bmi<=39.9:
        return 'Béo phì cấp độ 2'
    else:
        return 'Béo phì cấp độ 3'
def nguycobenh(bmi):
    if bmi<18.5:
        return 'Thấp'
    if bmi<=24.9:
        return 'Trung bình'
    if bmi<=29.9:
        return 'Cao'
    if bmi<=34.9:
        return 'Cao'
    if bmi<=39.9:
        return 'Rất cao'
    else:
        return 'Nguy hiểm'

print('Chương trình tính BMI')
height=float(input('Nhập vào chiều cao (m): '))
weight=float(input('Nhập vào cân nặng (kg): '))
bmi=BMI(height,weight)
print('BMI của bạn là:',bmi)
print('Phân loại của bạn:',PhanLoai(bmi))
print('Nguy cơ bệnh của bạn là:',nguycobenh(bmi))