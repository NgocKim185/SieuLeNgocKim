# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:31:20 2024

@author: Admin
"""

a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
#thực hiện phép tính
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là:", x)