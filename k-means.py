import matplotlib.pyplot as plt
import math
from random import randint

k = 3
clusters_changed = True
xs = []
ys = []
x_center = []
y_center = []
clusters = []

f = open("data.txt", "r")
for line in f:
  cord = line.strip().split('\t')
  xs.append(float(cord[0]))
  ys.append(float(cord[1]))
f.close()

plt.plot(xs,ys,'go')

n = len(xs)

# random dots
for d in range(k):
	x_dot = randint(int(min(xs)),int(max(xs)))
	y_dot = randint(int(min(ys)),int(max(ys)))
	x_center.append(x_dot)
	y_center.append(y_dot)
plt.plot(x_center,y_center,'ro')

# calc distances
for i in range(n):
	min_distance = 1000
	min_distance_cl = 0
	for cl in range(k):
		distance = math.sqrt(((xs[i]-x_center[cl])**2)+((ys[i]-y_center[cl])**2))
		if distance < min_distance:
			min_distance = distance
			min_distance_cl = cl
	clusters.append(min_distance_cl)
	line = plt.plot([xs[i],x_center[min_distance_cl]],[ys[i],y_center[min_distance_cl]])
	plt.setp(line, 'color', 'b', 'linewidth', 1.0)

plt.ylabel('Score')
plt.xlabel('ID')
plt.show()

while clusters_changed:
	new_clusters = []
	x_center_new = []
	y_center_new = []
	
	# new dots
	for d in range(k):
		count = 0
		x_sum = 0
		y_sum = 0
		for i in range(n):
			if clusters[i] == d:
				count += 1
				x_sum += xs[i]
				y_sum += ys[i]
		x_avr = x_sum/count
		y_avr = y_sum/count
		x_center_new.append(x_avr)
		y_center_new.append(y_avr)
		plt.annotate('New center', xy=(x_avr, y_avr), xytext=(25, 80),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	plt.plot(xs,ys,'go')
	plt.plot(x_center,y_center,'ro')
	
	plt.plot(x_center_new,y_center_new,'yo')
	plt.ylabel('Score')
	plt.xlabel('ID')
	plt.show()
	
	# calc clusters
	for i in range(n):
		min_distance = 1000
		min_distance_cl = 0
		for cl in range(k):
			distance = math.sqrt(((xs[i]-x_center_new[cl])**2)+((ys[i]-y_center_new[cl])**2))
			if distance < min_distance:
				min_distance = distance
				min_distance_cl = cl
		new_clusters.append(min_distance_cl)
		line = plt.plot([xs[i],x_center_new[min_distance_cl]],[ys[i],y_center_new[min_distance_cl]])
		plt.setp(line, 'color', 'b', 'linewidth', 1.0)
	
	if new_clusters == clusters:
		clusters_changed = False
		plt.title('Final graph')
		
	plt.plot(xs,ys,'go')
	plt.plot(x_center_new,y_center_new,'ro')
	plt.ylabel('Score')
	plt.xlabel('ID')
	plt.show()
	
	clusters = new_clusters