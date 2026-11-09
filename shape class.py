class shape:
    name="shape_name"
class Circle(shape):
    def area(self):
            r=int(input("enter r value: "))
            area_circle=3.14*r*r
            print("Area of the circle:",area_circle)
class rectangle(shape):
    def area(self):
            l=int(input("enter l value:"))
            b=int(input("enter b value:"))
            area_rectangle=l*b
            print("Area of the rectangle",area_rectangle)
class triangle(shape):
    def area(self):
        B=int(input("enter B value:"))
        h=int(input("enter h value:"))
        area_tri=0.5*B*h
        print("Area of the triangle",area_tri)
c=Circle()
R=rectangle()
t=triangle()
c.area()
R.area()
t.area()
    
    