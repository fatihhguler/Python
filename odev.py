points=[(1,2),(31,4),(12,22),(91,0),(10,11)]
def euclidianDistance(t1,t2):
    distance = (((t1[0]-t2[0])**2)+((t1[1]-t2[1])**2))**0.5
    return distance
distances=list()
for i in range(len(points)-1):
    for j in range(i+1,len(points)):
        distances.append(euclidianDistance(points[i],points[j]))
print(distances)
print(min(distances))

