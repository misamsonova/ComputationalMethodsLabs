import math

N = 10; M=3*N
a = -1; b = 1; x = 0; y = 0
mass_x = [x] * (N + 1); mass_x[0] = a; mass_x[-1] = b
mass_y = [y] * (N + 1)
mass_x2 = [x]*(M+1); mass_x2[0] = a; mass_x2[-1] = b
mass_y2 = [y] * (M + 1)
mass_zpl1 = [x]*(N+1)
mass_zpl2 = [x]*(M+1)
h = (b-a)/N
hh = (b-a)/M
print(h)
print(hh)
def function(z):
    res = (z ** 2 + 2) + math.sin(math.sqrt(z ** 2 + 2))
    return res

def lagrang_polinom(mass_x,mass_y,N,o):
    l=0.0;
    for i in range(0,N):
        q = 1.0;
        for j in range(0,N):
            if(j!=i):
                q =q*(o-mass_x[j])/(mass_x[i]-mass_x[j]);
        l=l+mass_y[i]*q
    return l;


for i in range(1,N):
    a = a+h
    mass_x[i] = a

for i in range(0, N+1):
    z = mass_x[i]
    mass_y[i] = function(z)

for i in range(0, N+1):
    print('Mass_1[', i,'] = ', mass_x[i])

for i in range(0, N+1):
    print('Mass_2[', i, '] = ', mass_y[i])

for i in range(0,N+1):
    o = mass_x[i]
    mass_zpl1[i] = lagrang_polinom(mass_x,mass_y,N,o)

a=-1
for i in range(1,M-1):
    a = a+hh
    mass_x2[i] = a

for i in range(0, M+1):
    print('Mass_x2[', i,'] = ', mass_x2[i])

for i in range(0, M+1):
    z = mass_x2[i]
    mass_y2[i] = function(z)

for i in range(0,M+1):
    o = mass_x2[i]
    mass_zpl2[i] = lagrang_polinom(mass_x2,mass_y2,M,o)

for i in range(0,M+1):
    d=abs(mass_zpl2[i] - mass_y2[i])
    print(f'{mass_x2[i]:25}',f'{mass_y2[i]:25}',f'{mass_zpl2[i]:25}',f'{d:20}', sep=" "*5)

mass_max = [1]
while min(mass_max)>0.01:
   for i in range(115,117):
        N2 = i; M2= 3*N2;
        print("N2 = ", N2)
        a=-1;b=1;x=0;y=0;
        mass_x_2=[x]*(M2+1);mass_x_2[0]=a;mass_x_2[-1]=b;
        mass_y_2=[y]*(M2+1)
        mass_zpl_2 = [x] * (M2 + 1)
        h2=(a-b)/M2
        mass_delta=[]

        for j in range(1,M2):
            a=a+h2
            mass_x_2[j]=a

        for j in range(0, M2 + 1):
            z = mass_x_2[j]
            mass_y_2[j] = function(z)

        for j in range(0, M2 + 1):
            o = mass_x_2[j]
            mass_zpl_2[j] = lagrang_polinom(mass_x_2, mass_y_2, M2, o)

        for j in range(0, M2 + 1):
            d = abs(mass_zpl_2[j] - mass_y_2[j])
            mass_delta.append(d)
        m = max(mass_delta)
        r = round(m,2)
        print(r)
        if max(mass_delta)<=0.01:
           print("THIS=>",r)