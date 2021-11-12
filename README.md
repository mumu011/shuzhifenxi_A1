
# 第一次数值分析大作业实验报


王觉 2019011371 自91

### 第一题

#### 数学推导

对于直角坐标系中的点(x,y)，其对应在极坐标中的点的坐标(x',y')如下：
$$
r=\frac{x}{W}*R\\
\theta=\frac{y}{H}*2\pi+\frac{\pi}{2}\\
x'=x_0+r\cos\theta\\
y'=y_0+r\sin\theta
$$
双线性插值：取距(x',y')最近的四个顶点为(x1,y1,data1) (x1,y2,data2) (x2,y1,data3) (x2,y2,data4)，进行双线性插值：
$$
r1=(x-x1)/(x2-x1)*data3+(x2-x)/(x2-x1)*data1\\
r2=(x-x1)/(x2-x1)*data4+(x2-x)/(x2-x1)*data2\\
data=(y-y1)/(y2-y1)*r2+(y2-y)/(y2-y1)*r1
$$

#### 误差分析

$f(x)\in C^2$，所以对于单线性插值，误差分析如下：
$$
R(x)=f(x)-P_1(x)=\frac{(x-x_0)(x-x_1)}{2}f''(\zeta)\\
|R(x)|\leq\frac{(x-x_0)(x-x_1)}{2}|maxf''(x)|\leq\frac{h^2}{8}|maxf''(x)|
$$
所以
$$
R_x(f)\leq\frac{h^2}{8}max|\frac{\partial^2 f_p}{\partial r^2}|\leq \frac{h^2}{8}M\\
R_y(f)\leq\frac{h^2}{8}max|\frac{\partial^2 f_p}{\partial \theta^2}|\leq \frac{h^2}{8}M\\
h=1\\
R(f)=R_x(f)+R_y(f)\leq \frac{h^2}{4}M=0.25M
$$
而在python计算中，计算sin值和cos值时会出现舍入误差，但python默认精度为17位小数，可以忽略不计；在最后计算灰度值时会将结果强制转换为整数，舍入误差小于等于0.5；在存储变量值时也会存在舍入误差，但python的默认精度为17位小数，可以忽略不计。

#### 作图结果

<img src="C:\Users\86213\Desktop\数值分析\第一次大作业\结果1.png" style="zoom:67%;" />

### 第二题

#### 数学推导

用三线性插值求出$D$中任一点的$SDF$近似值：取目标点(x,y,z)最近的8个顶点(x1,y1,z1,data1) (x1,y2,z1,data2) (x1,y1,z2,data3) (x1,y2,z2,data4) (x2,y1,z1,data5)(x2,y2,z1,data6) (x2,y1,z2,data7) (x2,y2,z2,data8)，进行三线性插值：
$$
r1=(x-x1)/(x2-x1)*data1+(x2-x)/(x2-x1)*data5\\
r2=(x-x1)/(x2-x1)*data2+(x2-x)/(x2-x1)*data6\\
r3=(x-x1)/(x2-x1)*data3+(x2-x)/(x2-x1)*data7\\
r2=(x-x1)/(x2-x1)*data4+(x2-x)/(x2-x1)*data8\\
\\
q1=(y-y1)/(y2-y1)*r2+(y2-y)/(y2-y1)*r1\\
q2=(y-y1)/(y2-y1)*r4+(y2-y)/(y2-y1)*r3\\
\\
data=(z-z1)/(z2-z1)*q2+(z2-z)/(z2-z1)*q1
$$
求出$N\ge10^3$个表面点的坐标：

首先通过某个阈值获取足够数量的给定点($\ge10^3$)的SDF尽量最小（代码中使用阈值为0.02，得到1306个点）

然后对于根据上述方法得到的每个点，以其为左下顶点可得到一个立方体，利用其x, y可以令插值表达式为零解出z，把(x,y,z)作为表面点（如果计算得到的z不在立方体中，则利用y,z求取x，如果计算得到的x不在立方体中，则利用x,z求取y）

由x,y求取表面点的坐标：
$$
surface\_x=(x1+x2)/2\\
surface\_y=(y1+y2)/2\\
\\
r1=(surface\_x-x1)/(x2-x1)*data1+(x2-surface\_x)/(x2-x1)*data5\\
r2=(surface\_x-x1)/(x2-x1)*data2+(x2-surface\_x)/(x2-x1)*data6\\
r3=(surface\_x-x1)/(x2-x1)*data3+(x2-surface\_x)/(x2-x1)*data7\\
r2=(surface\_x-x1)/(x2-x1)*data4+(x2-surface\_x)/(x2-x1)*data8\\
\\
q1=(surface\_y-y1)/(y2-y1)*r2+(y2-surface\_y)/(y2-y1)*r1\\
q2=(surface\_y-y1)/(y2-y1)*r4+(y2-surface\_y)/(y2-y1)*r3\\
\\
surface\_z=(z1*q2-z2*q1)/(q2-q1)
$$
由y,z或者x,z求取表面点的方法也是一样的

#### 误差分析

与上一题误差分析同理：
$$
R_x(f)\leq\frac{h^2}{8}max|\frac{\partial^2 f}{\partial x^2}|\leq \frac{h^2}{8}M\\
R_y(f)\leq\frac{h^2}{8}max|\frac{\partial^2 f}{\partial y^2}|\leq \frac{h^2}{8}M\\
R_z(f)\leq\frac{h^2}{8}max|\frac{\partial^2 f}{\partial z^2}|\leq \frac{h^2}{8}M\\
h=0.06\\
R(f)=R_x(f)+R_y(f)+R_z(f)\leq \frac{3h^2}{8}M=1.35\times10^{-3}M
$$
而在python计算中，在存储变量值时也会存在舍入误差，但python的默认精度为17位小数，可以忽略不计。

#### 作图结果 	

<img src="C:\Users\86213\Desktop\数值分析\第一次大作业\结果2.png" style="zoom:33%;" /> <img src="C:\Users\86213\Desktop\数值分析\第一次大作业\结果5.png" style="zoom:35%;" />

<img src="C:\Users\86213\Desktop\数值分析\第一次大作业\结果3.png" style="zoom:33%;" /> <img src="C:\Users\86213\Desktop\数值分析\第一次大作业\结果6.png" style="zoom:33%;" />

### 第三题

#### 数学推导

对于给定方程：
$$
(2x^2+y^2+z^2-1)^3+ax^2z^3+by^2z^3=0\\
$$
等价于：
$$
(2x^2+y^2+z^2-1)^3=-x^2z^3a-y^2z^3b
$$
对标最小二乘法标准形式$\varphi_0a+\varphi_1b=f$可取
$$
f=(2x^2+y^2+z^2-1)^3\\
\varphi_0=-x^2z^3\\
\varphi_1=-y^2z^3
$$
最小二乘法求解$a,b$等价于求解如下线性方程：
$$
(\varphi_0,\varphi_0)a+(\varphi_0,\varphi_1)b=(\varphi_0,f)\\
(\varphi_1,\varphi_0)a+(\varphi_1,\varphi_1)b=(\varphi_1,f)\\
$$
解得的$a,b$为：（保留两位有效数字）
$$
a=-0.10\\
b=-0.99
$$

#### 结果

![](C:\Users\86213\Desktop\数值分析\第一次大作业\结果4.png)

### 实验中遇到的问题

1. 第一题中(x,y)坐标取值和实际取值是反过来的，所以要进行变换
2. 第二题得到的表面点不够均匀，所以第三题计算得到的值可能误差比较大
3. 第一题恢复得到的二维码有些失真，可能是灰度值强制取整导致的

### 实验总结

通过本次实验，我对插值的理解更加深入了，同时在今后的生活中，也许也会遇到相似的问题可以通过插值来解决，还是非常有实际意义的。

### 文件结构

源代码：

第一题：QR_Code.py 

第二题：SDF.py 

第三题：LS.py

实验结果：

QR_CODE.png 第一题恢复得到的二维码 

surfaceXYZ.txt 第二题得到的表面点的坐标 

love.mlp 第二题重建的mesh文件
