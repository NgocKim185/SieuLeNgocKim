# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:14:43 2024

@author: Admin
"""

namsinh = int(input("Nhập năm sinh: "))
namhientai = 2024
if 0< namsinh <=2024:
    tuoi= namhientai - namsinh
    print("Tuổi của bạn là: ", tuoi)
else:
    print("Năm sinh không hợp lệ")    