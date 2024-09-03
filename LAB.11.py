# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:38:46 2024

@author: Admin
"""

ky_tu=input("Nhập một ký tự thường: ")
if len(ky_tu)==1 and ky_tu.islower():
    ky_tu_hoa=ky_tu.upper()
    print(f"Ký tự hoa là: {ky_tu_hoa}")
else:
    print("Nhập đúng 1 ký tự chữ thường.")    