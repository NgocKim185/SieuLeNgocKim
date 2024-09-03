# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:15:40 2024

@author: Admin
"""
import math
ban_kinh=float(input("Nhập bán kính của hình tròn: "))
chu_vi=2*math.pi*ban_kinh
dien_tich=ban_kinh**2*math.pi
print(f"Chu vi hình tròn là: {chu_vi:.2f}")
print(f"Diện tích hình tròn là: {dien_tich: .2f}")
