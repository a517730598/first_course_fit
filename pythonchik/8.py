from turtle import*


def f(n, l):
    if n==0:
        forward(l)
    else:
        f(n-1, l/2)
        left(60)
        f(n-1,l/4)
        f(n-1, -l/4)
        left(60)
        f(n-1, l/4)
        f(n-1, -l/4)
        right(120)
        f(n-1, l/2)


tracer(3)
f(4, 500)
done()