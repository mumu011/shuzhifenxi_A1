import numpy as np

if __name__ == "__main__":
    varphi_0 = []
    varphi_1 = []
    fx = []

    with open("surfaceXYZ.txt","r") as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            data = line.split(' ')
            x = float(data[0])
            y = float(data[1])
            z = float(data[2])
            varphi_0.append((x ** 2) * (z ** 3))
            varphi_1.append((y ** 2) * (z ** 3))
            fx.append(-1 * ((2 * (x ** 2) + (y ** 2) + (z ** 2) - 1) ** 3))

    varphi_0 = np.array(varphi_0)
    varphi_1 = np.array(varphi_1)
    fx = np.array(fx)

    a00 = np.dot(varphi_0, varphi_0)
    a01 = np.dot(varphi_1, varphi_0)
    a11 = np.dot(varphi_1, varphi_1)
    b0 = np.dot(varphi_0, fx)
    b1 = np.dot(varphi_1, fx)

    A = [[a00, a01],
         [a01, a11]]
    B = [b0, b1]

    r = np.linalg.solve(A, B)

    print(r)

