import numpy as np
import math
import xlwt


def Trilinear_interpolation(sdf_data, x, y, z):
    x_low = math.floor(x / 0.06) + 50
    x_high = x_low + 1
    y_low = math.floor(y / 0.06) + 50
    y_high = y_low + 1
    z_low = math.floor(z / 0.06) + 50
    z_high = z_low + 1

    x_RealLow = x_low * 0.06 - 3
    x_RealHigh = x_high * 0.06 - 3
    y_RealLow = y_low * 0.06 - 3
    y_RealHigh = y_high * 0.06 - 3
    z_RealLow = z_low * 0.06 - 3
    z_RealHigh = z_high * 0.06 - 3

    r1 = (x_RealHigh - x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_low][3] + (x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_low][3]
    r2 = (x_RealHigh - x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_low][3] + (x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_low][3]
    r3 = (x_RealHigh - x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_high][3] + (x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_high][3]
    r4 = (x_RealHigh - x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_high][3] + (x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_high][3]

    q1 = (y_RealHigh - y) / (y_RealHigh - y_RealLow) * r1 + (y - y_RealLow) / (y_RealHigh - y_RealLow) * r2
    q2 = (y_RealHigh - y) / (y_RealHigh - y_RealLow) * r3 + (y - y_RealLow) / (y_RealHigh - y_RealLow) * r4

    res = (z_RealHigh - z) / (z_RealHigh - z_RealLow) * q1 + (z - z_RealLow) / (z_RealHigh - z_RealLow) * q2

    return res

def getSurfaceXYZ(sdf_data, x, y, z):
    x_low = math.floor(x / 0.06) + 50
    x_high = x_low + 1
    y_low = math.floor(y / 0.06) + 50
    y_high = y_low + 1
    z_low = math.floor(z / 0.06) + 50
    z_high = z_low + 1

    x_RealLow = x_low * 0.06 - 3
    x_RealHigh = x_high * 0.06 - 3
    y_RealLow = y_low * 0.06 - 3
    y_RealHigh = y_high * 0.06 - 3
    z_RealLow = z_low * 0.06 - 3
    z_RealHigh = z_high * 0.06 - 3

    surface_x = (x_RealLow + x_RealHigh) / 2
    surface_y = (y_RealLow + y_RealHigh) / 2

    r1 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_low][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_low][3]
    r2 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_low][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_low][3]
    r3 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_high][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_high][3]
    r4 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_high][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_high][3]

    q1 = (y_RealHigh - surface_y) / (y_RealHigh - y_RealLow) * r1 + (surface_y - y_RealLow) / (y_RealHigh - y_RealLow) * r2
    q2 = (y_RealHigh - surface_y) / (y_RealHigh - y_RealLow) * r3 + (surface_y - y_RealLow) / (y_RealHigh - y_RealLow) * r4

    surface_z = (z_RealHigh * q1 - z_RealLow * q2) / (q1 - q2)

    if(abs(surface_z - z) > 0.06):
        surface_z = (z_RealLow + z_RealHigh) / 2
        surface_y = (y_RealLow + y_RealHigh) / 2

        r1 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * sdf_data[x_low][y_low][z_low][3] + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * sdf_data[x_low][y_low][z_high][3]
        r2 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * sdf_data[x_low][y_high][z_low][3] + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * sdf_data[x_low][y_high][z_high][3]
        r3 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * sdf_data[x_high][y_low][z_low][3] + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * sdf_data[x_high][y_low][z_high][3]
        r4 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * sdf_data[x_high][y_high][z_low][3] + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * sdf_data[x_high][y_high][z_high][3]

        q1 = (y_RealHigh - surface_y) / (y_RealHigh - y_RealLow) * r1 + (surface_y - y_RealLow) / (y_RealHigh - y_RealLow) * r2
        q2 = (y_RealHigh - surface_y) / (y_RealHigh - y_RealLow) * r3 + (surface_y - y_RealLow) / (y_RealHigh - y_RealLow) * r4

        surface_x= (x_RealHigh * q1 - x_RealLow * q2) / (q1 - q2)

    if (abs(surface_x - x) > 0.06):
        surface_z = (z_RealLow + z_RealHigh) / 2
        surface_x = (x_RealLow + x_RealHigh) / 2

        r1 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_low][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_low][3]
        r2 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_low][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_low][3]
        r3 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_low][z_high][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_low][z_high][3]
        r4 = (x_RealHigh - surface_x) / (x_RealHigh - x_RealLow) * sdf_data[x_low][y_high][z_high][3] + (surface_x - x_RealLow) / (x_RealHigh - x_RealLow) * sdf_data[x_high][y_high][z_high][3]

        q1 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * r1 + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * r3
        q2 = (z_RealHigh - surface_z) / (z_RealHigh - z_RealLow) * r2 + (surface_z - z_RealLow) / (z_RealHigh - z_RealLow) * r4

        surface_y = (y_RealHigh * q1 - y_RealLow * q2) / (q1 - q2)

    return [surface_x,surface_y,surface_z]

if __name__ == "__main__":
    sdf_data = np.load('sdf.npy')

    # print(sdf_data)
    # print(Trilinear_interpolation(sdf_data,-1,-1,-1))

    # 求取表面点
    _list = []
    for i in range(0,101):
        for j in range(0,101):
            for k in range(0,101):
                if(abs(sdf_data[i][j][k][3]) <= 0.02):
                    _list.append(sdf_data[i][j][k])

    # print(len(_list))
    # print(_list)

    _surface = []
    for data in _list:
        _surface.append(getSurfaceXYZ(sdf_data,data[0],data[1],data[2]))

    # surface_xlx = xlwt.Workbook(encoding='utf-8')
    # surface_worksheet = surface_xlx.add_sheet('surfaceXYZ')
    #
    # for i in range(0,len(_surface)):
    #     surface_worksheet.write(i, 0, _surface[i][0])
    #     surface_worksheet.write(i, 1, _surface[i][1])
    #     surface_worksheet.write(i, 2, _surface[i][2])
    #
    # surface_xlx.save('surfaceXYZ.xls')

    with open("surfaceXYZ.txt","w") as f:
        for i in range(0,len(_surface)):
            f.write(str(_surface[i][0]) + ' ' + str(_surface[i][1]) + ' ' + str(_surface[i][2]) + '\n')

    # print(_surface)

