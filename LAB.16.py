# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:56:19 2024

@author: Admin
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
tong_giay=gio*3600+phut*60+giay
if 0<=1<24 and 0<=phut<60 and 0<=giay<60:
    print("Tổng giây là: ", tong_giay)
else:
    print("Giờ, phút, giây không hợp lệ")    