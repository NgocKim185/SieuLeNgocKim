# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:33:00 2024

@author: Admin
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b*b - 4*a*c
if delta == 0:
    x = -b / 2*a
    print("PT có nghiệm kép là: ",x)
elif delta < 0:
    print("PT vô nghiệm")
if delta > 0:
    n1=(-b + delta**0.5) / (2*a)
    n2=(-b - delta**0.5) / (2*a)
    print("PT có 2 nghiệm phân biệt {n1} và {n2}.")