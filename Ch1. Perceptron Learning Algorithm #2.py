import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

""" Implementing the Perceptron Learning Algorithm. """
# Next step is to try with negative xn!

x_range = 10; trials = 100; 
x = []; y = []; x1_p = []; x2_p = []; x1_n = []; x2_n = []; 
eta = 0.1; m = []; c = []; w = [0.1 ,0.1, 0.9]; 
t = 0; xy = []; etaxy = [];	m_x = np.arange(0,10,0.1); m_y = []; opt = []; mm_y = pd.DataFrame(); 

for i in range(0, trials):
	x1 = random.randint(1, x_range)
	r = random.uniform(-1,1)
	if r >= 0:
		y.append(+1)
		x2 = random.randint(3,4)*x1
		x1_p.append(x1)
		x2_p.append(x2)
	else: 
		y.append(-1)
		x2 = (random.randint(0,1)*x1)
		x1_n.append(x1)
		x2_n.append(x2)
	x.append([1,x1,x2])

#print('t\t', 'x\t\t', 'w\t\t\t', 'y\t' ,'w*x\t\t', 'xy\t')

while t < len(x):

	signal = (np.dot(w,x[t]))
	if (y[t]*signal) > 0:
		w = w
	else:
		xy = list(map(lambda i: (y[t]*i),x[t]))  
		etaxy = list(map(lambda i: i*eta,xy))
		w  = [(i+j) for i, j in zip(w, etaxy)]

	m.append(float(-w[1]/w[2]))
	c.append(float(-w[0]/w[2]))
	#print(t,'\t', x[t],'\t', w, '\t\t', y[t],'\t', signal, '\t', xy, '\n')
	t += 1
	
	
for i in range(0, len(m_x)):
	opt.append(2*m_x[i])

for j in range(0,len(x)):
	for i in range(0, len(m_x)):
		m_y.append(m[j]*m_x[i] + c[j])
	mm_y[j] = pd.Series(m_y)
	m_y = []

for j in range(0, len(x)):
	plt.plot(x1_p, x2_p, 'bo', x1_n, x2_n, 'gx')
	plt.plot(m_x, opt, 'r-')
	plt.plot(m_x, mm_y[j], 'b-')

plt.plot(m_x, mm_y[j], 'y-')
plt.show()
print(w)










