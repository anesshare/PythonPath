import sys #Biblioteka da bi gui mogao da bude prikazan i da se ne gasi odmah
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel ,QVBoxLayout,QHBoxLayout,QGridLayout,QWidget,QPushButton,QCheckBox,QRadioButton,QButtonGroup,QLineEdit #biblioteka za gui
from PyQt5.QtGui import QIcon,QFont,QPixmap   #biblioteka za ikonicu prozora,font,sliku
from PyQt5.QtCore import Qt

#BOILERPLATE
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool gui") #Metoda za title aplikacije
        self.setGeometry(700,300,600,600) #Postavljanje sirine visine i pozicije guia
        self.setWindowIcon(QIcon('C:/Users/aness/OneDrive/Radna površina/fotke/arena5')) #Za ikonicu prozora
        label = QLabel("Hello World!",self)
        label.setGeometry(0,0,600,500)
        label.setFont(QFont("Arial",30))
        label.setStyleSheet("color: blue;""background-color:red;""font-weight:bold;")
        label.setWordWrap(True)
        self.button = QPushButton("Click me!",self)
        self.checkBox = QCheckBox("Check me!",self)
        label.setAlignment(Qt.AlignCenter)
        self.radio1 = QRadioButton("Visa",self)
        self.radio2 = QRadioButton("Master",self)
        self.radio3 = QRadioButton("Paypal",self)
        self.btnGrp = QButtonGroup(self)
        self.btnGrp2 = QButtonGroup(self)
        self.lineEdit = QLineEdit(self) #INPUT
        self.lineBtn = QPushButton("Submit",self)

        self.initUI()
      
        # pixmap = QPixmap("logo.jpg")
        # label.setPixmap(pixmap)
        # label.setScaledContents(True) #Da slika bude kao i velicina labela
        
    def initUI(self):
        # centralWidget = QWidget()
        # self.setCentralWidget(centralWidget)
        # hBox = QVBoxLayout()
        # label2 = QLabel("Hello !")
        # hBox.addWidget(label2)
        # centralWidget.setLayout(hBox)
        ############# OVO JE ZA GRID
        self.button.setGeometry(300,300,200,200)
        self.checkBox.setGeometry(100,200,400,400)
        self.checkBox.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.onClick)
        self.checkBox.stateChanged.connect(self.checkChanged)
        self.radio1.setGeometry(0,0,200,50)
        self.radio2.setGeometry(50,50,200,50)
        self.radio3.setGeometry(100,100,200,50)
        self.btnGrp.addButton(self.radio1)
        self.btnGrp.addButton(self.radio2)
        self.btnGrp2.addButton(self.radio3)     #DELIMO RADIO BUTTONE U GRUPE DA BI MOGLO VISE DA SE STIKLIRA
        self.radio1.toggled.connect(self.radioChanged)      
        self.radio2.toggled.connect(self.radioChanged)      
        self.radio3.toggled.connect(self.radioChanged)      
        self.lineEdit.setGeometry(200,0,300,100)
        self.lineEdit.setStyleSheet("font-size:25px;""font-family:arial;")
        self.lineBtn.setGeometry(500,0,100,40)
        self.lineBtn.setStyleSheet("font-size:25px;""font-family:arial;")
        self.lineBtn.clicked.connect(self.submit)
    def onClick(self):
        print("Hellooo")
        self.button.setText("clicked")
    def checkChanged(self,state):       #Checkbutton
        if state == Qt.Checked:
            print("you like food")
        else:
            print("you dont like food")
    def radioChanged(self):
        radioBtn = self.sender()#ovaj button prima sta je kliknuto i ispisuje
        if radioBtn.isChecked():
            print(f"Button {radioBtn.text()} is selected")
    def submit(self):
        print("he")
        text = self.lineEdit.text()
        print(f"Hello {text}")
def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #Da ne bi prozor nestajao odmah ovo mora ovako 

if __name__ == "__main__":
    main()