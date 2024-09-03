# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:52:52 2024

@author: Admin
"""

a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
c=int(input("Nhập số nguyên c: "))
d=int(input("Nhập số nguyên d: "))
so_nho_nhat=a #Giả sử
if b<so_nho_nhat:
    so_nho_nhat=b
if c<so_nho_nhat:
    so_nho_nhat=c
if d<so_nho_nhat:
    so_nho_nhat=d
print(f"Số nhỏ nhất là: {so_nho_nhat}")    