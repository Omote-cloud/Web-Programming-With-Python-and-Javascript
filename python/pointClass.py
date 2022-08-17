class Point():
    #A method defining how to create a point
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p = Point(2,3)

print(f"{p.x},{p.y}")
print(p.x)