# a = int(input('请输入大于等于3的数\n'))
# fib1 = 1
# fib2 = 0
# fib3 = 1
# for i in range(a):
#     print(fib3)
#     fib3 = fib1 + fib2
#     fib2 = fib1
#     fib1 = fib3


n = int(input('input:\n'))  # 获取输入
print('==== 递归 ====')
def fab(n):  # 递归函数，计算第n项的值
    if n == 1 or n == 2:
        return 1
    return fab(n-1) + fab(n-2)

result = []
for x in range(1, n+1):
    result.append(str(fab(x)))
print(result)
print('\n'.join(result))  # 输出结果