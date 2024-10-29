n = int(input('Введите число от 3 до 20: '))
a = range(1,n)
result = []
for i in range(1):
    result.append([])
    for j in range(len(a[0:n])):
        for g in range (len(a[0:n])):
            if a[g] == a[j]:
                break
            if n%(a[g]+a[j]) == 0:
                        result.extend([[a[g],a[j]]])
print ('Получите пары отмычек для кода:',result[1:])
