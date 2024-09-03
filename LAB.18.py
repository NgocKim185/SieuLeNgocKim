# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:08:52 2024

@author: Admin
"""
gio_thu_1=input("Nhập giờ thứ nhất (hh:ss:mm): ")
gio_thu_2=input("Nhập giờ thứ hai (hh:ss:mm): ")
hh, mm, ss =map(int, gio_thu_1.split(":"))
h, m, s = map(int, gio_thu_2.split(":"))
tong_giay_1=hh*3600+mm*60+ss
tong_giay_2=h*3600+m*60+s
hieu_thoi_gian = tong_giay_1 - tong_giay_2
if hieu_thoi_gian > 0:
    h1=hieu_thoi_gian//3600
    m1=(hieu_thoi_gian%3600)// 60
    s1= hieu_thoi_gian%60
    print(f"Hiệu của 2 thời gian là: {h1}:{m1}:{s1}")
else:
    print("Thời gian nhỏ hơn")
tong_thoi_gian=tong_giay_1+tong_giay_2
h2=tong_thoi_gian//3600
m2=(tong_thoi_gian%3600)//60
s2=tong_thoi_gian%60
print(f"Tổng của 2 thời gian là: {h2}:{m2}:{s2}")    
