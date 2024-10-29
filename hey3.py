import itertools
import random
import matplotlib.pyplot as plt


a = int(input("how many cities?"))
cities = []
for b in  range(a):
    i = random.randint(1,10)
    j = random.randint(1,10)
    c = [i , j]
    cities.append(c)
print(cities)

start = int(input("from which city?"))
print("start ity will be" , cities[start])

def gr(cities , start):
    routes = list(itertools.permutations(cities))
    routes2 = []
    for r in routes:
        if r[0] == cities[start]:
            r = list(r)
            r.append(cities[start])
            routes2.append(r)
        else:
            continue
    for x in routes2:
        print(x)
    return routes2

def masafn(t , y):
    x = (((t[0]-y[0])**2)+((t[1]-y[1])**2))**0.5
    return x

def mosafk(o):
    z = 0
    for p in range(len(o)-1):
        m = masafn(o[p],o[p+1])
        z += m
    return z

allroutes = gr(cities, start)
mini = []
for rot in allroutes:
    g = mosafk(rot)
    mini.append(g)
    
print(min(mini))
minim = mini.index(min(mini))
print(minim)





plt.figure(figsize=(8,8))
plt.xlim(0,15)
plt.ylim(0,15)
plt.xlabel("x")
plt.ylabel("y")
plt.title("traveling selsman")


for t , (x , y) in enumerate(cities):
    if t == start:
        plt.scatter(x, y,color="red")
    else:    
        plt.scatter(x, y,color="blue")
    plt.text(x+0.25, y, f"city{t}" , fontsize=12 , ha="left")
    
    
    
    
    
    
    
for index, o in enumerate(allroutes):
    xc = [point[0] for point in o]
    yc = [point[1] for point in o]
    if index == minim:
        plt.plot(xc,yc, color="purple", linestyle="-", lw=2, marker="s",ms=8,mec="red",mfc="black",alpha=1)
    else:    
        plt.plot(xc,yc, color="green", linestyle="-", lw=2, marker="s",ms=8,mec="red",mfc="black",alpha=0.0)


plt.show()