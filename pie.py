pi = 3.14

def calc_circle_area(r):
    return pi*r*r

def calc_circumference(r):
    return 2*pi*r

r=float(input("pls input ur circle radius : "))
circle_area = calc_circle_area(r)
circumference = calc_circumference(r)
print("ur circle area: {0:0.2f}, ur circumference : {1:0.2f}".format(circle_area, circumference))