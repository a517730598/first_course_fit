from turtle import*


def bin_tree(n, l, ang):
    if n != 0:
        forward(l)
        right(ang)
        bin_tree(n-1, l/1.5, ang)
        left(2 * ang)
        bin_tree(n-1, l/1.5, ang)
        right(ang)
        forward(-l)


bin_tree(3, 30, 50)
done()