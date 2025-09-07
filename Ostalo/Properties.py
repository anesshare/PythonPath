class Rectangle:
    def __init__(self,width,height):
        self._width = width         #Kad stavimo ovo ovako _width znaci da su private atributi 
        self._height = height
    @property
    def width(self):
        return f"{self._width:.1f}cm" #Geteri metode
    @property
    def height(self):
        return f"{self._height:.1f}cm" #Get isto
    @width.setter       #Setteri
    def width(self,newWidth): 
        if newWidth > 0:
            self._width = newWidth
        else: 
            print("Width must be > 0")
    @height.setter
    def height(self,newHeight):
        if newHeight > 0:
            self._height = newHeight
        else: 
            print("Width must be > 0")
    @width.deleter          #bRISANJE VREDNOSTI ATRIBUTA
    def width(self):
        del self._width
        print(":D")
rect = Rectangle(3,4)
rect.width = 5
del rect.width
