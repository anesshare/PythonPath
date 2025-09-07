import mysql.connector
import sys
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QApplication
from PyQt5.QtCore import Qt
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="C:/Users/aness/OneDrive/Radna površina/Py/Python/DataBase/.env.example")

class DBConnector:
    def __init__(self):
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
            print("fail")
    def createUser(self,username,password):
        query = "INSERT into pythonprac (username,password) VALUES(%s,%s)"
        self.cursor.execute(query,(username,password))
        self.connection.commit()
        print("Korisnik dodat!")
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.ime = QLabel("Unesite username",self)
        self.inp1 = QLineEdit(self)
        self.naslov = QLabel("REGISTRACIJA",self)
        self.pw = QLabel("Unesite password:",self)
        self.inp2 = QLineEdit(self)
        self.btn = QPushButton("Potvrdi",self)
        self.btn2 = QPushButton("Login",self)
        self.setWindowTitle("PyRegister")
        self.initUI()
    def initUI(self):
        self.db = DBConnector()
        self.setStyleSheet("font-family:Sans-Serif;""font-size:20px;")
        vbox = QVBoxLayout(self)
        self.inp2.setEchoMode(QLineEdit.Password)
        vbox.addWidget(self.naslov)
        self.naslov.setStyleSheet("font-weight:bold;")
        self.naslov.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.ime)
        vbox.addWidget(self.inp1)
        self.ime.setAlignment(Qt.AlignCenter)
        self.pw.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.pw)
        vbox.addWidget(self.inp2)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.btn2)
        self.setLayout(vbox)
        self.btn.clicked.connect(self.addUser)
        self.btn2.clicked.connect(self.displayLogin)

    def addUser(self):
        user = self.inp1.text()
        loz = self.inp2.text()    
        if user and loz:
            self.db.createUser(user,loz)
            print("Success")
            self.inp1.clear()
            self.inp2.clear()
        else:
            print("postoje prazna pojla")        
    def displayLogin(self):
        from LoginDB import Login
        self.loginPage = Login()
        self.loginPage.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register = Register()
    register.show()
    sys.exit(app.exec_())
