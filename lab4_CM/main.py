import math

def euler_method(f, a, b, h, y0):
    n = int((b-a)/h)
    x = [a]
    y = [y0]
    for i in range(n):
        x[i]=a+i*h
        x.append(x[i] + h)
        y.append(y[i] + h * f(x[i], y[i]))
    return x, y

def f(x, y):
    return x*y

a = 0
b = math.sqrt(2)
N = 32
h = (b - a) / N
y0 = 1

x, y = euler_method(f, a, b, h, y0)
for i in range(len(x)):
    print(f'x = {x[i]}, y = {y[i]}')

def analytical_solution(a, b, N):
    h = (b - a) / N
    x = a
    y = []

    for i in range(N + 1):
        y_i = math.exp((x ** 2) / 2)
        y.append(y_i)
        x += h

    return y


a = 0
b = math.sqrt(2)

solution = analytical_solution(a, b, N)
print(solution)
print()

for i in range(N+1):
    d = math.fabs(y[i]-solution[i])
    print("X = ",f'{x[i]:25}',"Y = ",f'{y[i]:25}',"Anal. Y = ",f'{solution[i]:25}',"Delta = ",f'{d:25}', sep=" "*2)

print()
print("___________")
print()
for i in range(1,1000):
    N = i
    def euler_method(f, a, b, h, y0):
        z = int((b - a) / h)
        x = [a]
        y = [y0]
        for i in range(z):
            x[i] = a + i * h
            x.append(x[i] + h)
            y.append(y[i] + h * f(x[i], y[i]))
        return x, y

    def f(x, y):
        return x * y


    a = 0
    b = math.sqrt(2)
    h = (b - a) / N
    y0 = 1

    x, y = euler_method(f, a, b, h, y0)
    def analytical_solution(a, b, N):
        h = (b - a) / N
        x = a
        y = []

        for i in range(N + 1):
            y_i = math.exp((x ** 2) / 2)
            y.append(y_i)
            x += h

        return y


    solution = analytical_solution(a, b, N)
    k=0
    for j in range(N):
        if math.fabs(solution[j]-y[j])<0.01:
            k+=1
    if k== len(y):
        for j in range(N):
            print("S = ", f'{solution[j]:25}', "Y[i] = ", f'{y[j]:25}', "Delta = ", f'{round(math.fabs(solution[j]-y[j]),3):25}', sep=" " * 2)
        print("N = ", N)
        break
    else:
        continue