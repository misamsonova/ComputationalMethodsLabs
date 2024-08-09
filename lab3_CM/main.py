import math

a = 0; b = 1;
x = 0; y = 0; N = 16;
mass_x = [x] * (N + 1)
mass_y = [y] * (N + 1)
mass_x[0] = a
mass_x[-1] = b
mass_zpl1 = [x] * (N + 1)
h = (b - a) / N
def function(z):
    res = math.sqrt(z)
    return res

def integrate(a,b):
    area = (2*(b**(3/2))/3)-((2*(a**(3/2)))/3)
    return area

def method_right_rectangle(mass_y):
    integral_sum=0
    for i in range(1,N+1):
        integral_sum+=mass_y[i]
    res = integral_sum * h
    return res

def method_left_rectangle(mass_y):
    integral_sum = 0
    for i in range(0, N):
        integral_sum += mass_y[i]
    res = integral_sum * h
    return res

def trapezoid_method(mass_y):
    res = 0
    for i in range(N):
        res += ((mass_y[i]+mass_y[i+1])*h)/2
    return res

def method_Simpson(mass_y):
    sum1 = sum([mass_y[i] for i in range(1, N, 2)])  # сумма значений функции на нечетных узлах
    sum2 = sum([mass_y[i] for i in range(2, N, 2)])  # сумма значений функции на четных узлах
    res = h / 3 * (mass_y[0] + 4 * sum1 + 2 * sum2 + mass_y[-1])
    return res

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
res_1 = method_right_rectangle(mass_y)
res_2 = trapezoid_method(mass_y)
res_3 = method_Simpson(mass_y)
res_4 = method_left_rectangle(mass_y)
res_5 = integrate(0, 1)
print()
print("#2....")
print("N = ", N)
print("N:", N, "I:", res_5, "I_l:", res_4, "I_r:", res_1, "I_t:", res_2, "I_s:", res_3, sep=" " * 3)
print()

for i in range(3):
    N = int(input("N = "))
    a=0;b=1;
    mass_x[0] = a
    mass_x[-1] = b
    mass_x = [x] * (N + 1)
    mass_y = [y] * (N + 1)
    mass_zpl1 = [x] * (N + 1)
    h = (b - a) / N

    for i in range(1, N):
        a = a + h
        mass_x[i] = a

    for i in range(0, N + 1):
        z = mass_x[i]
        mass_y[i] = function(z)
    a = 0;
    b = 1;
    res_1 = method_right_rectangle(mass_y)
    res_2 = trapezoid_method(mass_y)
    res_3 = method_Simpson(mass_y)
    res_4 = method_left_rectangle(mass_y)
    res_5 = integrate(0, 1)
    print("N:", N, "I:", res_5, "I_l:", res_4, "I_r:", res_1, "I_t:", res_2, "I_s:", res_3, sep=" " * 3)
    print()
print()
print("#3....")
for j in range(1,1000):
    N = j
    a = 0;
    b = 1;
    mass_x[0] = a
    mass_x[-1] = b
    mass_x = [x] * (N + 1)
    mass_y = [y] * (N + 1)
    mass_zpl1 = [x] * (N + 1)
    h = (b - a) / N
    for i in range(1, N):
        a = a + h
        mass_x[i] = a

    for i in range(0, N + 1):
        z = mass_x[i]
        mass_y[i] = function(z)

    res_1 = method_left_rectangle(mass_y)
    res_5 = integrate(0, 1)
    ost = res_5 - res_1
    if (ost<0.001):
        print("M = ", N)
        k = 0
        for i in range(N-2,N+2):
            k+=1
            N = i
            a = 0; b = 1;
            mass_x[0] = a
            mass_x[-1] = b
            mass_x = [x] * (N + 1)
            mass_y = [y] * (N + 1)
            mass_zpl1 = [x] * (N + 1)
            h = (b - a) / N
            for i in range(1, N):
                a = a + h
                mass_x[i] = a

            for i in range(0, N + 1):
                z = mass_x[i]
                mass_y[i] = function(z)

            res_1 = method_left_rectangle(mass_y)
            print("K = ",k,"N = ", N, "I = ", res_5, "I_l = ", res_1, "|I-I_l| = ", math.fabs(res_5-res_1))
        break
    else:
        continue
print()
print("#4....")
for j in range(1,1000):
    N = j
    a = 0;
    b = 1;
    mass_x[0] = a
    mass_x[-1] = b
    mass_x = [x] * (N + 1)
    mass_y = [y] * (N + 1)
    mass_zpl1 = [x] * (N + 1)
    h = (b - a) / N
    for i in range(1, N):
        a = a + h
        mass_x[i] = a

    for i in range(0, N + 1):
        z = mass_x[i]
        mass_y[i] = function(z)

    res_1 = method_right_rectangle(mass_y)
    res_5 = integrate(0, 1)
    ost = res_5 - res_1
    if (ost<0.001):
        print("M = ", N)
        k = 0
        for i in range(N-2,N+2):
            k+=1
            N = i
            a = 0; b = 1;
            mass_x[0] = a
            mass_x[-1] = b
            mass_x = [x] * (N + 1)
            mass_y = [y] * (N + 1)
            mass_zpl1 = [x] * (N + 1)
            h = (b - a) / N
            for i in range(1, N):
                a = a + h
                mass_x[i] = a

            for i in range(0, N + 1):
                z = mass_x[i]
                mass_y[i] = function(z)

            res_1 = method_right_rectangle(mass_y)
            print("K = ",k,"N = ", N, "I = ", res_5, "I_l = ", res_1, "|I-I_l| = ", math.fabs(res_5-res_1))
        break
    else:
        continue

print()
print("#5....")
for j in range(1,1000):
    N = j
    a = 0;
    b = 1;
    mass_x[0] = a
    mass_x[-1] = b
    mass_x = [x] * (N + 1)
    mass_y = [y] * (N + 1)
    mass_zpl1 = [x] * (N + 1)
    h = (b - a) / N
    for i in range(1, N):
        a = a + h
        mass_x[i] = a

    for i in range(0, N + 1):
        z = mass_x[i]
        mass_y[i] = function(z)

    res_1 = trapezoid_method(mass_y)
    res_5 = integrate(0, 1)
    ost = res_5 - res_1
    if (ost<0.001):
        print("M = ", N)
        k = 0
        for i in range(N-2,N+2):
            k+=1
            N = i
            a = 0; b = 1;
            mass_x[0] = a
            mass_x[-1] = b
            mass_x = [x] * (N + 1)
            mass_y = [y] * (N + 1)
            mass_zpl1 = [x] * (N + 1)
            h = (b - a) / N
            for i in range(1, N):
                a = a + h
                mass_x[i] = a

            for i in range(0, N + 1):
                z = mass_x[i]
                mass_y[i] = function(z)

            res_1 = trapezoid_method(mass_y)
            print("K = ",k,"N = ", N, "I = ", res_5, "I_l = ", res_1, "|I-I_l| = ", math.fabs(res_5-res_1))
        break
    else:
        continue

print()
print("#6....")
for j in range(1,1000):
    N = j
    a = 0;
    b = 1;
    mass_x[0] = a
    mass_x[-1] = b
    mass_x = [x] * (N + 1)
    mass_y = [y] * (N + 1)
    mass_zpl1 = [x] * (N + 1)
    h = (b - a) / N
    for i in range(1, N):
        a = a + h
        mass_x[i] = a

    for i in range(0, N + 1):
        z = mass_x[i]
        mass_y[i] = function(z)

    res_1 = method_Simpson(mass_y)
    res_5 = integrate(0, 1)
    ost = res_5 - res_1
    if (ost<0.001):
        print("M = ", N)
        k = -6
        for i in range(N-4,N+4,2):
            k+=2
            N = i
            a = 0; b = 1;
            mass_x[0] = a
            mass_x[-1] = b
            mass_x = [x] * (N + 1)
            mass_y = [y] * (N + 1)
            mass_zpl1 = [x] * (N + 1)
            h = (b - a) / N
            for i in range(1, N):
                a = a + h
                mass_x[i] = a

            for i in range(0, N + 1):
                z = mass_x[i]
                mass_y[i] = function(z)

            res_1 = method_Simpson(mass_y)
            print("K = ",k,"N = ", N, "I = ", res_5, "I_l = ", res_1, "|I-I_l| = ", math.fabs(res_5-res_1))
        break
    else:
        continue