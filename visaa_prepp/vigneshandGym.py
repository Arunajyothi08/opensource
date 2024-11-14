x, y, z = map(int,input().split())
if x <= z:
    print("2")
elif x+y <= z:
    print("1")
else:
    print("0")
