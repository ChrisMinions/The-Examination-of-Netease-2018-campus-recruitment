'''
[编程题] 字符串碎片
时间限制：1秒
空间限制：32768K
一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,
请你帮助计算这个字符串的所有碎片的平均长度是多少。

输入描述:
输入包括一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),s只含小写字母('a'-'z')


输出描述:
输出一个整数,表示所有碎片的平均长度,四舍五入保留两位小数。

如样例所示: s = "aaabbaaac"
所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25

输入例子1:
aaabbaaac

输出例子1:
2.25
'''

'''
解题思路：遍历字符串
  遍历字符串，找到所有碎片的长度
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

s = input()
length = len(s)
results = []
count = 1
for i in range(length-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        results.append(count)
        count = 1
results.append(count)

print("%.2f" % (sum(results)/len(results)))
