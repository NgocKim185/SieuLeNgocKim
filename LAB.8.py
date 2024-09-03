# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:20:30 2024

@author: Admin
"""

can_nang=float(input("Nhập cân nặng: "))
chieu_cao=float(input("Nhập chiều cao: "))
bmi=can_nang/chieu_cao**2
print("Chỉ số BMI của bạn là: ", bmi)
if bmi<18.5:
    print("Bạn bị thiếu cân.")
elif 18.5<=bmi<24.9:
    print("Bạn có cân nặng bình thường.")
elif 25<=bmi<29.9:
    print("Bạn bị thừa cân.")
else:
    print("Bạn bị béo phì.")    