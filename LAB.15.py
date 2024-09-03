# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:33:12 2024

@author: Admin
"""

import math
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
ab=a*b
can_a=math.sqrt(a)
can_b=math.sqrt(b)
can3_a=math.pow(a,1/3)
can3_b=math.pow(b,1/3)
can3_ab=math.pow(ab,1/3)
x1=((a+b)/(can3_a+can3_b))-can3_ab
x2=(can3_a + can3_b)*(can3_a + can3_b)
ket_qua=x1/x2
print("Kết quả là: ", ket_qua)
number=ket_qua
print("Kết quả sau làm tròn", round(ket_qua, 3))