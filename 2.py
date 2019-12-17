"Обернена послідовність"
print("Введіть через Enter послідовність чисел, вона завершиться \n після введення нуля : ")
a = list()
while True:
    x = float(input())
    if x == 0: break
    a.append(x)
b=list(reversed(a))
print("Вихідна послідовність: ",a)
print("Обернена послідовність: ",b)
