#Practical 1B:Calculate the output of neural net using both binary and bipolar sigmoidal function.
import math
print("Practical Performed by: Om Solanki , Roll No : 04")


x1=0.3
x2=0.5
x3=0.6
print("Value of x1= ",x1)
print("Value of x2= ",x2)
print("Value of x3= ",x3)
w1=0.2
w2=0.1
w3=-0.3
print("Value of w1= ",w1)
print("Value of w2= ",w2)
print("Value of w3= ",w3)
yin=x1*w1 + x2*w2 + x3*w3
print("Net Input :",yin)

#Applying Binary Sigmoidal function
funct_x1= 1/(1+math.exp(-yin))
print("After applying sigmoidal function: ",funct_x1)


#Applying Bipolar Sigmoidal function
funct_x2= (1-math.exp(-yin))/(1+math.exp(-yin))
print("After applying Bipolar sigmoidal function: ",funct_x2)
