from turtle import*


def f(n,l):
    if n==0:
        forward(l)
    else:
        f(n-1, l/2)
        left(90)
        f(n-1,l/4)
        f(n-1, -l/4)
        right(90)
        f(n-1, l/2)


tracer(3)
f(3, 50)
done()