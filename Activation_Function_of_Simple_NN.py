# Prac 1A:-Design a simple linear neural network model
# Task:- Calculate Net Input Apply and Activation Function


print("Practical Performed by: Om Solanki , Roll No : 04")
print("Enter the value of x1:-")
x1 = float(input())
print("Enter the value of x2:-")
x2 = float(input())
print("Enter the value of w1:-")
w1 = float(input())
print("Enter the value of w2:-")
w2 = float(input())
print("Calculating Net Input: ")
net_input = x1 * w1 + x2 * w2
print("Net Input : ", net_input)
print("Applying Activation Function:")
threshold = 0
if net_input >= threshold:
    print("1")
else:
    print("0")
