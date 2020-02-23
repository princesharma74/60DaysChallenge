# GCD Studied from Coursera 'Algorithmic Toolbox'
m = input().split()
def GCD(a, b):
    if b==0:
        return a
    return GCD(b, a%b)
print(GCD(int(m[0]), int(m[1])))
