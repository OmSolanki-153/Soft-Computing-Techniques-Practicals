print("Practical performed by Roll No.:04 Om Solanki")

X = [[0,0], [1,0], [0,1], [1,1]]
print("Inputs = ")
for x in X:
    print(x)
Y = [1,-1,-1,-1]
print("Target = ",Y)
w = [0,0]
print("Initial weight values = ", w)
for i in range(len(X)):
    for j in range(len(w)):
        w[j] = w[j] + X[i][j] + Y[i]
print(i, "Iteration, Weight values = ",w)
