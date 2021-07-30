class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(x1, y1, x2, y2, fill= "green")
        
    def move(self, x, y):
        self.center= [x, y]
        
myClass = Circle([10, 30], 320)
print("Center: " + str(myClass.center))