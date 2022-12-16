def f(n):
    for i in range(0, len(n) - 1):
        minn = i
        for j in range(i + 1, len(a)):
            if n[j] < n[minn]:
                minn = j
        n[i], n[minn] = n[minn], n[i]
a = [int(x) for x in open('rt.txt')]
f(a)
print('сортированный список: ', end='')
print(a)
