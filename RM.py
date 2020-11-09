import numpy as np
from math import exp
f = np.array([500,300,200])
# capacity
C = 100
# time of iteration
T = 600	
# No. of class
classes = np.array([0,1,2])

mu = np.array([0.001,0.015,0.05])
vu = np.array([0.01,0.005,0.0025])
# value function & initialize
V = np.empty((C+1,T+1,3))

print("===")
#print(V.shape)

for i in range(C+1):
	for j in range(3):
		V[i,T,j] = 0
V[0] = 0

#for each time level
for t in reversed(range(T)):
	#for each capacity level
	#print(t)s
	for x in range(1,C+1):
		#print(x)
		#for each class
		for j in classes:
			prob_acc = 0
			prob_rej = 1
			prob_ini = 0
			max_revenue = 0

			# probibilities of accepting & rejecting each price of class
			# this could be a for loop since the probabilities may be accumulated
			# because when price is in class3, people in class1 and class2 are also
			# williing to pay
			# here !!!!! focus j+1
			for i in range(j+1):
				prob_ini = mu[i]*exp(vu[i]*t)
				prob_acc = prob_acc + prob_ini
				prob_rej = prob_rej - prob_ini
			total_revnue = 0

			# get revenue by given popularities
			# ============ for avoiding price drop : for loop should be range(j,3) ============
			for k in range(0,3):
				total_revnue = prob_acc*(f[j]+V[x-1,t+1,k])  + prob_rej*V[x,t+1,k]
				if (total_revnue > max_revenue):
					max_revenue = total_revnue
			V[x,t,j] = max_revenue

expected_revenue = np.max(V)
print(expected_revenue)
print("==============")

