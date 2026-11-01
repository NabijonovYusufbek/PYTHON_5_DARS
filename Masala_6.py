def ijobiy_yigindi(*sonlar):
    return sum(x for x in sonlar if x > 0)


son = list(map(int,input().split()))
print(ijobiy_yigindi(*son))