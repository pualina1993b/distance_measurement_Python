import math
ax = int(input("ax="))
ay = int(input("ay="))
az = int(input("az="))
bx = int(input("bx="))
by = int(input("by="))
bz = int(input("az="))
dx = bx - ax
dy = by - ay
dz = bz - az
l = math.sqrt(math.pow(dx,2) + math.pow(dy,2) + math.pow(dz,2))
print("A(" + str(ax) + ", " + str(ay) + ", " + str(az) + ")" + " B(" + str(bx) + ", " + str(by) + ", " + str(bz) + ")")
print("l= "+str(l))


