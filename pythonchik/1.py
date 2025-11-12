from turtle import*

def cvadratik(n, l):
    if n == 0:
        pass
    else:
        for _ in range(5):
            fd(l)
            lt(90)
        lt(10)
        up()
        fd(l/5)
        down()
        cvadratik(n-1, l*0.8)

tracer(0)
cvadratik(30, 300)
done()
