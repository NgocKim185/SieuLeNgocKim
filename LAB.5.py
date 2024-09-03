# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:11:15 2024

@author: Admin
"""

gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
if 0<=gio<24 and 0<=phut<60 and 0<=giay<60:
    tong_giay = gio * 3600 + phut * 60 + giay
    print("Tổng số giây là: ", tong_giay)
else:
    print("Giờ, phút hoặc giây không hợp lệ")