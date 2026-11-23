#HILL CLIMBING
def f(x):
    return a*x*x + b*x + c

a, b, c = map(float, input("Enter a, b, c: ").split())
x = float(input("Enter initial x: "))
step = float(input("Enter step size: "))

if a >= 0 or step <= 0:
    print("Enter a negative 'a' and positive step size")
else:
    while True:
        next_x = max([x-step, x+step], key=f)

        if f(next_x) <= f(x):
            break

        x = next_x

    print("Maximum x:", round(x, 4))
    print("Maximum value:", round(f(x), 4))