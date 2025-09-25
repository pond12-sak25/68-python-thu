class calculate_area:
    def retangele_area(self, w, h):
        return w * h
    
    @classmethod
    def triagle_area(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r
    
cal = calculate_area()
cal_rec = cal.retangele_area(4, 5)
cal_tri = cal.triagle_area(4, 5)
cal_cir = cal.circle_area(5)

print("Area of Rectangle:", cal_rec)
print("Area of Triangle:", cal_tri)
print("Area of Circle:", cal_cir)
#prnt(calculate_area.trianle(5 , 10))
#print(calculate_area.circle(7))
#print(calculate_area.retangle(5, 10))