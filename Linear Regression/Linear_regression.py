import numpy as np 
import matplotlib.pyplot as plt
print("Program For Linear regression : ")
temp=int(input("\n\nEnter number of data inputs : ")) 
x=[]
y=[]
while temp>0:
  temp=temp-1
  temp_x,temp_y=[int(k) for k in input("Enter x and y : ").split()]
  x.append(temp_x)
  y.append(temp_y)
x=np.array(x)
y=np.array(y)  
#calculating effective mean
n=np.size(x)
a=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x*x)-np.sum(x)*np.sum(x))
b=(np.sum(x*x)*np.sum(y)-np.sum(x)*np.sum(x*y))/(n*np.sum(x*x)-np.sum(x)*np.sum(x))
print("\n\n m = ",a," c = ",b)
#plotting
y_line=a*x+b
plt.scatter(x,y,color="m")
plt.plot(x,y_line,color="g")
plt.ylabel('Dependent Variable(y)')
plt.xlabel('Independent Variable(x)')
plt.show()
