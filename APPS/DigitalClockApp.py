import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTime,QTimer,Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(500,500,500,200)
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-family:Arial;""font-size:100px;""color:green;""font-weight:bold;")
        self.setStyleSheet("background:black;")
        self.timer.timeout.connect(self.updateTime) #AZURIRA SAT SVAKE SEKUNDE
        self.timer.start(1000)
        self.updateTime()
    def updateTime(self):
        currTime = QTime.currentTime().toString("hh:mm:ss AP") #UZIMA TRENUTNO VREME I PRETVARA U STRING
        self.timeLabel.setText(currTime) #DODAJEMO U LABEL KAO STRING TRENUTNO VREME
if __name__== "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())