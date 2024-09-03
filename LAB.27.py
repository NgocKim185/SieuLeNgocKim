# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:55:02 2024

@author: Admin
"""
import math
hinh=input("Nhap hinh: ")
"n" == "Hinh chữ nhật"
"v" == "Hình vuông"
"t" == "Hình tròn"
if hinh == "n":
    print("Tính chu vi và diện tích hình chữ nhật")
    a=int(input("Nhập chiều dài: "))
    b=int(input("Nhập chiều rộng: "))
    chu_vi=(a+b)*2
    dien_tich=a*b
    print(f"Kết quả là: {chu_vi} {dien_tich}")
elif hinh == "v":
    print("Tính chu vi và diện tich hình vuông")
    a=int(input("Nhập chiều dài cạnh: "))
    chu_vi=a*4
    dien_tich=a*a
    print(f"Kết quả là: {chu_vi} {dien_tich}")
else:
    print("Tính chu vi và diện tich hình vuông")
    r=int(input("Nhập bán kính: "))
    chu_vi=2*math.pi*r
    dien_tich=math.pi*r**2
    print(f"Kết quả là: {chu_vi} {dien_tich}")
    