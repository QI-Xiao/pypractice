aaa = range(1,5)
for i in aaa:
    for j in aaa:
        for k in aaa:
            if j != i and j != k and i != k:
                print(str(i)+str(j)+str(k))

