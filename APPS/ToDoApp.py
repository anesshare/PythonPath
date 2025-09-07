import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QHBoxLayout,QWidget,QLabel,QLineEdit,QPushButton,QListWidget
from PyQt5.QtCore import Qt

class Todo(QWidget):
    def __init__(self):
        super().__init__()
        self.inp = QLineEdit(self)
        self.submit = QPushButton("POTVRDI",self)
        self.text = QLabel("Unesite zadatke: ",self)
        self.setWindowTitle("TODO")
        self.deleteBtn = QPushButton("IZBRISI",self)
        self.storeText = QListWidget(self)
        self.initUI()


    def initUI(self):
        self.setStyleSheet("font-family: Segoe UI; font-size: 28px;""background:#2C2F5D;")
        self.inp.setStyleSheet("padding:10px;""font-size:30px;""font-weight:bold;""border-radius:20px;""background:#F5F0E6;")
        self.deleteBtn.setStyleSheet("background:#C4E86B;""color:#2C2F5D;""font-weight:bold;""border-radius:20px")
        self.storeText.setStyleSheet("background:#F5F0E6")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("color:#FFFFFF")
        self.submit.setStyleSheet("background:#C4E86B;""color:#2C2F5D;""font-weight:bold;""border-radius:20px")
        self.inp.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.text)
        vbox.addWidget(self.inp)
        vbox.addWidget(self.submit)
        vbox.addWidget(self.deleteBtn)
        vbox.addWidget(self.storeText)
        self.setLayout(vbox)
        self.submit.clicked.connect(self.displayText)
        self.deleteBtn.clicked.connect(self.deleteText)

    def displayText(self):
        contain = self.inp.text()
        if contain == "":
            pass
        else:
            self.storeText.addItem(contain)
            self.inp.setText("")
    def deleteText(self):
        listItems = self.storeText.selectedItems()
        if listItems:
            for item in listItems:
                self.storeText.takeItem(self.storeText.row(item))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo = Todo()
    todo.show()
    sys.exit(app.exec_())