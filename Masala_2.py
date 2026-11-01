def katta_son(a, b):
    if a > b:
        return a
    else:
        return b

a,b = map(int,input().split())
print(f"Eng katta son {katta_son(a,b)}")