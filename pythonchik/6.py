from turtle import*

#tracer(0)

def mokr(n,l):
    if n == 0:
        fd(l)
    else:
        mokr(n-1, l/3)
        lt(90)
        mokr(n-1, l/3)
        rt(90)
        mokr(n-1, l/3)
        rt(90)
        mokr(n-1,2 * l/3)
        lt(90)
        mokr(n-1, l/3)
        lt(90)
        mokr(n-1, l/3)
        rt(90)
        mokr(n-1, l/3)

mokr(2, 400)
done()