# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:59:56 2024

@author: Admin
"""

a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
c=int(input("Nhập số nguyên c: "))
d=int(input("Nhập số nguyên d: "))
so_lon_nhat=a #Giả sử
if b>so_lon_nhat:
    so_lon_nhat=b
if c>so_lon_nhat:
    so_lon_nhat=c
if d>so_lon_nhat:
    so_lon_nhat=d
print(f"Số lớn nhất là: {so_lon_nhat}")