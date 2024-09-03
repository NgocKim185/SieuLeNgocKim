# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:47:48 2024

@author: Admin
"""

def sap_xep_ba_so(a,b,c):
    if a>b:
        a, b=b, a
    if b>c:
        b, c=c, b
    if a>b:
        a, b=b, a
    return a,b,c
#Nhập ba số
a=float(input("Nhap so a: "))
b=float(input("Nhap so b: "))
c=float(input("Nhap so c: "))
a,b,c=sap_xep_ba_so(a, b, c)
print(f"Cac so theo thu tu tang dan: {a}, {b}, {c}")

    