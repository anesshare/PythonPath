import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QHBoxLayout,QPushButton,QVBoxLayout
from PyQt5.QtCore import QTimer, QTime,Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.timeLabel = QLabel("00:00:00:00",self)
        self.startBtn = QPushButton("START",self)
        self.stopBtn = QPushButton("STOP",self)
        self.resetBtn = QPushButton("RESET",self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("STOPWATCH")
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
     
        self.setLayout(vbox)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.startBtn)
        hbox.addWidget(self.stopBtn)
        hbox.addWidget(self.resetBtn)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
            QPushButton,QLabel{
            padding:20px;
            font-weight:bold;   
            font-family:Colibri
                        }
            QPushButton{
            font-size:30px;          
                           }
            QLabel{
             font-size:120px;
             background:#4a76c2;       
            border-radius:20px;
                           }
        """)
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)
        self.resetBtn.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateDisplay)
        
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.timeLabel.setText(self.formatTime(self.time))
    def formatTime(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milis = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milis:02}"
    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())