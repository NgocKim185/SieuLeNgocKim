# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:06:58 2024

@author: Admin
"""

N=int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    Hang_chuc = N//10
    Hang_don_vi = N % 10
    Tong = Hang_chuc + Hang_don_vi
    print("Tổng các chữ số của N là: " ,Tong)
else:
    print("Nhập số nguyên dương có 2 chữ số!") 