import numpy as np
import cv2
import math

# 读取图片
img = cv2.imread('qr-polar.png')
# 获取原图的宽
a = img.shape[0]
# 获取原图的高
b = img.shape[1]
# 获取原图的RGB通道数
c = img.shape[2]

# 中心位置
p0 = a // 2
print((a, b, c))
new_img = np.ones((a, b, c), dtype="u1")


for x in range(a):
    for y in range(b):
        # 计算r和theta
        r = x * p0 / a
        theta = 2 * math.pi * y / b + math.pi / 2
        
        # 找到对应坐标
        px = r * math.cos(theta) + p0
        py = r * math.sin(theta) + p0
        
        # 双线性插值
        px1 = int(r * math.cos(theta) + p0)
        py1 = int(r * math.sin(theta) + p0)
        px2 = px1 + 1
        py2 = py1 + 1
        fq11 = img[px1, py1, :]
        fq21 = img[px2, py1, :]
        fq12 = img[px1, py2, :]
        fq22 = img[px2, py2, :]
        fr1 = (px2 - px) / (px2 - px1) * fq11 + (px - px1) / (px2 - px1) * fq21
        fr2 = (px2 - px) / (px2 - px1) * fq12 + (px - px1) / (px2 - px1) * fq22
        f = (py2 - py) / (py2 - py1) * fr1 + (py - py1) / (py2 - py1) * fr2
        
        # 赋值
        new_img[x,y,:] = f

cv2.imwrite('new.png',new_img)




