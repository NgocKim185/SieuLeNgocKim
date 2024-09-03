# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:21:35 2024

@author: Admin
"""
number=int(input("Nhập một số nguyên: "))
if number == 0:
    print("Không")
elif number == 1:
    print("Một")   
elif number == 2:
    print("Hai")
elif number == 3:
    print("Ba")   
elif number == 4:
    print("Bốn") 
elif number == 5:
    print("Năm")   
elif number == 6:
    print("Sáu")   
elif number == 7:
    print("Bảy") 
elif number == 8:
    print("Tám")   
elif number == 9:
    print("Chín")   
else:
    print("Không đọc được")    
so_tu_0_den_9= {0: "Khong", 1: "Mot", 2: "Hai", 3: "Ba", 4: "Bon", 5: "Nam", 6: "Sau", 7: "Bay", 8: "Tam", 9: "Chin"}
nhap=int(input("Nhập một số nguyên: "))
if nhap in so_tu_0_den_9:
    print(so_tu_0_den_9[nhap])   
else:
    print("Không đọc được")    