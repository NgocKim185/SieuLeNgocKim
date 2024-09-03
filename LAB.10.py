# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:35:51 2024

@author: Admin
"""

so_xe=input("Nhập số xe (4 chu so): ")
def tinh_so_nut(so_xe):
    tong_chu_so = sum(int(chu_so) for chu_so in so_xe)
    so_nut= tong_chu_so % 10
    return so_nut
if len(so_xe) == 4 and so_xe.isdigit():
    so_nut=tinh_so_nut(so_xe)
    print(f"Số xe {so_xe} có số nút là: {so_nut}")
else:
    print("Vui lòng nhập đúng 4 chữ số")    