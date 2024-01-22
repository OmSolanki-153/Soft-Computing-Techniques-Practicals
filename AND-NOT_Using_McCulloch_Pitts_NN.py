# Generate AND/NOT function using McCulloch-Pitts neural net.
print("Practical performed by Om Solanki Roll No.:04")


num_ip=int(input("enter the no of inputs "))
w1=1
w2=1
print("for the",num_ip,"inputs calculates the net input")
x1=[]
x2=[]
for i in range(0,num_ip):
    e1=int(input("x1="))
    e2=int(input("x2="))
    x1.append(e1)
    x2.append(e2)
    print("x1=",x1)
    print("x2=",x2)
    n=[w1*i for i in x1]
    m=[w2*i for i in x2]
    Yin=[]
for i in range(0,num_ip):
    Yin.append(n[i]+m[i])
print("\n Excitetory weight")
print("Yin=",Yin)

#Assume one weight as excitetory and one as inhibitory
w1=1
w2=-1
n=[w1*i for i in x1]
m=[w2*i for i in x2]
Yin=[]
for i in range(0,num_ip):
    Yin.append(n[i]+m[i])
print("\n Excitetory weight")
print("Yin=",Yin)
print("\n after assuming one weight as excitetory and one as inhibitory")
y=[]
for i in range(0,num_ip):
    if(Yin[i]>=1):
        e=1
        y.append(e)
    if(Yin[i]<1):
        e=0
        y.append(e)
    print("y=",y)
