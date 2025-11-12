from turtle import*

#tracer(0)
def koh(n, l):
    if n == 0:
        fd(l)
    else:
        koh(n-1, l/3)
        left(60)
        koh(n-1, l/3)
        right(120)
        koh(n-1, l/3)
        left(60)
        koh(n-1, l/3)

def cneg(n, l):
    koh(n, l)
    rt(120)
    koh(n, l)
    rt(120)
    koh(n, l)
    rt(120)

cneg(2, 400)
done()