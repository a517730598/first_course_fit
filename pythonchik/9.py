from turtle import*

def fractal(n, l):
    if n == 0:
        forward(l)
    else:
        left(45)
        fractal(n-1, l/2)
        right(90)
        fractal(n-1, l/2)
        left(45)


tracer(3)
fractal(8, 1800)
done()