# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:36:42 2024

@author: Admin
"""
gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
def kiem_tra_thoi_gian(gio, phut, giay):
    if 0<=gio<24 and 0<=phut<60 and 0<=giay<60:
        return("Gio, phut, giay hợp lệ")
    else:
        return("Gio, phut, giay không hợp lệ")
ket_qua=kiem_tra_thoi_gian(gio, phut, giay)    
print(ket_qua)