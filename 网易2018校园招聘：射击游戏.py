'''
[编程题] 射击游戏
时间限制：1秒
空间限制：32768K
小易正在玩一款新出的射击游戏,这个射击游戏在一个二维平面进行,小易在坐标原点(0,0),平面上有n只怪物,
每个怪物有所在的坐标(x[i], y[i])。小易进行一次射击会把x轴和y轴上(包含坐标原点)的怪物一次性消灭。
小易是这个游戏的VIP玩家,他拥有两项特权操作:
1、让平面内的所有怪物同时向任意同一方向移动任意同一距离
2、让平面内的所有怪物同时对于小易(0,0)旋转任意同一角度
小易要进行一次射击。小易在进行射击前,可以使用这两项特权操作任意次。
小易想知道在他射击的时候最多可以同时消灭多少只怪物,请你帮帮小易。


所有点对于坐标原点(0,0)顺时针或者逆时针旋转45°,可以让所有点都在坐标轴上,所以5个怪物都可以消灭。

输入描述:
输入包括三行。
第一行中有一个正整数n(1 ≤ n ≤ 50),表示平面内的怪物数量。
第二行包括n个整数x[i](-1,000,000 ≤ x[i] ≤ 1,000,000),表示每只怪物所在坐标的横坐标,以空格分割。
第二行包括n个整数y[i](-1,000,000 ≤ y[i] ≤ 1,000,000),表示每只怪物所在坐标的纵坐标,以空格分割。


输出描述:
输出一个整数表示小易最多能消灭多少只怪物。

输入例子1:
5
0 -1 1 1 -1
0 -1 -1 1 1

输出例子1:
5
'''

'''
解题思路：寻找垂直线
  利用已知的点，寻找两条相互垂直的直线，使落在这条直线上的点最多，点的数量就是小易最多能消灭的怪物数量
  先选出两个点连成一条直线，然后选出第三个点，这第三个点不能和前两个点重合，也不能在前两个点连成的直线上
  之后去找第四个点，如果第四个点在前两个点所连成的直线上，或者和第三个点组成的直线与上一条直线垂直，则记数变量加1
  遍历完后所有情况后，输出最大的记数变量即可
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为40.00%
'''

def main():
    n = int(input())

    x_cords = [i for i in map(int, input().split())]
    y_cords = [j for j in map(int, input().split())]

    max_ = -1
    for i1 in range(n):
        for i2 in range(i1+1, n):
            dx_12 = x_cords[i1] - x_cords[i2]
            dy_12 = y_cords[i1] - y_cords[i2]
            for i3 in range(n):
                dx_13 = x_cords[i1] - x_cords[i3]
                dy_13 = y_cords[i1] - y_cords[i3]
                if i3 == i1 or dy_12*dx_13 == dy_13*dx_12:
                    continue
                else:
                    count = 0
                    for i4 in range(0, n):
                        dx_14 = x_cords[i1] - x_cords[i4]
                        dy_14 = y_cords[i1] - y_cords[i4]
                        dx_34 = x_cords[i3] - x_cords[i4]
                        dy_34 = y_cords[i3] - y_cords[i4]
                        if dy_12*dx_14 == dy_14*dx_12 or dx_12*dx_34 == -dy_12*dy_34:
                            count += 1
                    if max_ < count:
                        max_ = count

    if max_ == -1:
        max_ = n
    print(max_)

if __name__ == '__main__':
    main()
