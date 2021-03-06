'''
[编程题] 游历魔法王国
时间限制：1秒
空间限制：32768K
魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,
请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。 
输入描述:
输入包括两行,第一行包括两个正整数n(2 ≤ n ≤ 50)和L(1 ≤ L ≤ 100),表示城市个数和小易能行动的次数。
第二行包括n-1个整数parent[i](0 ≤ parent[i] ≤ i), 对于每个合法的i(0 ≤ i ≤ n - 2),
在(i+1)号城市和parent[i]间有一条道路连接。


输出描述:
输出一个整数,表示小易最多能游历的城市数量。

输入例子1:
5 2
0 1 2 3

输出例子1:
3
'''

'''
解题思路：理解题意+分析问题
  理解题意：输入第二行的意思实际上说的是第i+1号城市的上一个城市，例如 0 0 1 1 ，意思为第1,2号城市上一个城市
  是0号城市，第3,4号城市上一个城市是1号城市
  分析问题：尽量不走回头路，所以要先找到树中最长的那条分支
            首先找到树中最长的那条分支，得到它的长度，将长度与L比较比较，若长度大于L，则直接输出L，不用走回头路
            若L大于长度，则在走最长分支之前，我们还剩余L-长度的步数，这些步数可以访问其他城市，不过访问其他城市
            时需要走回头路，所以能访问的城市数量是：（L-长度）//2，将上值和长度的和即为最多能访问的城市，
            当然，也得考虑城市遍历完后L步数还没用光的情况。
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

N, L = map(int, input().split())

parents = [int(i) for i in input().split()]

nodes_depth = [0] * N

for i in range(N-2):
    nodes_depth[i+1] = nodes_depth[parents[i]] + 1

max_depth = max(nodes_depth)

if L <= max_depth:
    max_cities = L + 1
else:
    max_cities = max_depth + ((L - max_depth) // 2) + 1

if max_cities <= N:
    print(max_cities)
else:
    print(N)
