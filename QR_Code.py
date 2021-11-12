import numpy as np
from PIL import Image
import cv2
import math

# img 原图 destW 目标图像的宽 destH 目标图像的高
def bilinear_interpolation(img, destW, destH, rgb):
    dst = np.ones((destW, destH, rgb),dtype=int)

    srcW = img.shape[0]
    srcH = img.shape[1]

    ox = srcW // 2
    oy = srcH // 2

    R = srcW // 2

    for i in range(0,destW):
        for j in range(0,destH):
            r = i / destW * R
            theta = j / destH * 2 * math.pi + math.pi / 2

            x = r * math.cos(theta) + ox
            y = r * math.sin(theta) + oy

            x_low = math.floor(x)
            x_high = x_low + 1
            y_low = math.floor(y)
            y_high = y_low + 1

            # 双线性插值
            r1 = (x_high - x) / (x_high - x_low) * img[x_low,y_low,:] + (x - x_low) / (x_high - x_low) * img[x_high,y_low,:]
            r2 = (x_high - x) / (x_high - x_low) * img[x_low,y_high,:] + (x - x_low) / (x_high - x_low) * img[x_high,y_high,:]
            res = (y_high - y) / (y_high - y_low) * r1 + (y - y_low) / (y_high - y_low) * r2

            dst[i,j,:] = res

    return dst

if __name__ == "__main__":
    img_path = 'qr-polar.png'
    image = cv2.imread(img_path)
    # print(image)
    srcW = image.shape[0]
    srcH = image.shape[1]
    rgb = image.shape[2]
    dst = bilinear_interpolation(image,image.shape[0] // 2,image.shape[1] // 2,rgb)
    # print(dst)
    cv2.imwrite('QR_CODE.png',dst)