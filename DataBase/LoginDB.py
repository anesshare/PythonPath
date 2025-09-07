import mysql.connector
import sys
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QApplication,QMessageBox
from PyQt5.QtCore import Qt
from RegisterDB import Register
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="C:/Users/aness/OneDrive/Radna površina/Py/Python/DataBase/.env.example")
class DBConnection:
    def __init__(self):
        super().__init__()
        self.connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            port = int(os.getenv("DB_PORT")),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASS"),
            database = os.getenv("DB_NAME")
        )
        if self.connection.is_connected():
            print("Uspeh")
            self.cursor = self.connection.cursor()
        else:
            print("Fail")
    def fetchUser(self,username,password):
        query =  f"SELECT username,password from pythonprac WHERE username= '{username}' AND password = '{password}'"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        return res


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.naslov = QLabel("LOGIN",self)
        self.username = QLabel("Unesite username",self)
        self.input1 = QLineEdit(self)
        self.password = QLabel("Unesite password:",self)
        self.input2 = QLineEdit(self)
        self.button = QPushButton("Potvrdi",self)
        self.btn2 = QPushButton("Registracija",self)
        self.setWindowTitle("PyLogin")
        self.initUI()
    def initUI(self):
        self.db = DBConnection()
        self.setStyleSheet("font-family:Sans-Serif;""font-size:20px;")
        vbox = QVBoxLayout(self)
        self.input2.setEchoMode(QLineEdit.Password)
        vbox.addWidget(self.naslov)
        self.naslov.setAlignment(Qt.AlignCenter)
        self.naslov.setStyleSheet("font-weight:bold;")
        vbox.addWidget(self.username)
        vbox.addWidget(self.input1)
        self.username.setAlignment(Qt.AlignCenter)
        self.password.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.password)
        vbox.addWidget(self.input2)
        vbox.addWidget(self.button)
        vbox.addWidget(self.btn2)
        self.button.clicked.connect(self.getUser)
        self.btn2.clicked.connect(self.openReg)
        self.setLayout(vbox)
        
    def getUser(self):
        username = self.input1.text()
        password = self.input2.text()
        res = self.db.fetchUser(username,password)
        if res:
            QMessageBox.information(self,"Uspeh","Uspesno ste se logovali")
            self.input1.clear()
            self.input2.clear()
            self.close()
        else:
            QMessageBox.warning(self,"Greska","Netacne login informacije!")
            self.input1.clear()
            self.input2.clear()
    def openReg(self):
        self.openReg = Register()
        self.openReg.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
