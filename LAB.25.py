# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:46:24 2024

@author: Admin
"""
chu_cai=input("Nhập chữ cái: ")
def chuyen_doi_chu_cai(chu_cai):
    if 'a'<=chu_cai<='z':
        return chu_cai.upper()
    elif 'A'<=chu_cai<='Z':
        return chu_cai.lower()
    else:
        return "Ky tu khong hop le"
ket_qua=chuyen_doi_chu_cai(chu_cai)
print(ket_qua)    