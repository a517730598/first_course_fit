from turtle import*

#tracer(0)
def koh(n, l):
    if n == 0:
        fd(l)
    else:
        koh(n-1, l/3)
        lt(60)
        koh(n-1, l/3)
        rt(120)
        koh(n-1, l/3)
        lt(60)
        koh(n-1, l/3)

koh(2, 400)
done()