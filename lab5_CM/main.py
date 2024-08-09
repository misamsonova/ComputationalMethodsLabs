import math


def runge_kutta(f, a, b, y0, h):
    n = int((b - a) / h)  # Количество шагов
    x = [a]  # Массив значений x
    y = [y0]  # Массив значений y
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y.append(y[i] + 0.5 * h * (k1 + k2))
        x.append(x[i] + h)
    return x, y
def f(x, y):
    return x*y

a = 0
b = math.sqrt(2)
N = 32
h = (b - a) / N
y0 = 1

x, y = runge_kutta(f,a,b,y0,h)
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

for i in range(N):
    d = math.fabs(y[i]-solution[i])
    print("X = ",f'{x[i]:25}',"Y = ",f'{y[i]:25}',"Anal. Y = ",f'{solution[i]:25}',"Delta = ",f'{d:25}', sep=" "*2)

print()
print("___________")
print()
for i in range(1,1000):
    N = i


    def runge_kutta(f, a, b, y0, h):
        n = int((b - a) / h)  # Количество шагов
        x = [a]  # Массив значений x
        y = [y0]  # Массив значений y
        for i in range(n):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + h, y[i] + h * k1)
            y.append(y[i] + 0.5 * h * (k1 + k2))
            x.append(x[i] + h)
        return x, y


    a = 0
    b = math.sqrt(2)
    h = (b - a) / N
    y0 = 1

    x, y = runge_kutta(f,a,b,y0,h)
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