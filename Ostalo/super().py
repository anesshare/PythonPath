
class Shapes:
  def __init__(self,color,filled,):
        self.color = color
        self.filled = filled

class Circle(Shapes):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
class Square(Shapes):
       def __init__(self,color,filled,width):
         super().__init__(color,filled)
         self.width = width
class Triangle(Shapes):
       def __init__(self,color,filled,width,height):
            super().__init__(color,filled)
            self.width = width
            self.height = height

triangle = Triangle("blue",False,6,2)
print(triangle.color)
print(triangle.filled)
print(triangle.width)
print(triangle.height)