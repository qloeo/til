point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

X_min = min(point1[0],point2[0],point3[0])
Y_min = min(point1[1],point2[1],point3[1])
X_max = max(point1[0],point2[0],point3[0])
Y_max = max(point1[1],point2[1],point3[1])
# print(X_min,Y_min,X_max,Y_max)

rp1 = [X_min, Y_min]
rp2 = [X_max, Y_min]
rp3 = [X_min, Y_max]
rp4 = [X_max, Y_max]
# print(rp1,rp2,rp3,rp4)

if rp1 != point1 and rp1 != point2 and rp1 != point3:
    print(int(rp1[0]),int(rp1[1]))
elif rp2 != point1 and rp2 != point2 and rp2 != point3:
    print(int(rp2[0]),int(rp2[1]))
elif rp3 != point1 and rp3 != point2 and rp3 != point3:
    print(int(rp3[0]),int(rp3[1]))
else :
    print(int(rp4[0]),int(rp4[1]))