import sys
import requests
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QHBoxLayout,QWidget,QLabel,QLineEdit,QPushButton
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter city name:",self)
        self.textBox = QLineEdit(self)
        self.getWButton = QPushButton("GET WEATHER",self)
        self.temperature = QLabel(self)
        self.desc = QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("WEATHER APP")
        vbox = QVBoxLayout()
        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.textBox)
        vbox.addWidget(self.getWButton)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.desc)
        self.setLayout(vbox)
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.textBox.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.desc.setAlignment(Qt.AlignCenter)
        self.cityLabel.setObjectName("cityLabel")
        self.textBox.setObjectName("textbox")
        self.getWButton.setObjectName("getWButton")
        self.temperature.setObjectName("temperature")
        self.desc.setObjectName("desc")
        self.setStyleSheet("""
        QLabel,QPushButton{
            font-family:calibri;
                           }
        QLabel#cityLabel{
            font-size:40px;
            font-style:italic;
                           }
        QLineEdit#textbox{
        font-size:40px;
                           }
        QPushButton{
        font-size:30px;
        font-weight:bold;
                           }
        QLabel#temperature{
        font-size:30px;
                           }
        QLabel#desc{
        font-size:50px;color:blue;
                           }
        """)
        self.getWButton.clicked.connect(self.getWeather)
    def getWeather(self):
        apiKey = "521201a8c1366ce78cd083bae8b36b4e"
        city = self.textBox.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            data = resp.json()
            if data["cod"] == 200:
                self.displayWeather(data)
        except requests.exceptions.HTTPError:
                match resp.status_code:
                     case 400:
                          self.displayErr("Bad request")
                     case 401:
                          self.displayErr("Unauthorized")
                     case 403:
                          self.displayErr("Access denied")
                     case 404:
                          self.displayErr("Not found")
                     case 500:
                          self.displayErr("Internal server error")
                     case 502:
                          self.displayErr("Bad gateway")
                     case 503:
                          self.displayErr("Service unavailable")
                     case _:
                          self.displayErr("Something went wrong...")

        except requests.exceptions.RequestException:
                pass
        except requests.exceptions.ConnectionError:
             print("No connection")
        except requests.exceptions.Timeout:
             print("Timeout error")
             self.temperature.setStyleSheet("font-size:30px")
    def displayErr(self,msg):
        self.temperature.setText(msg)
    def displayWeather(self,data):
        temp = data["main"]["temp"]
        tempC = temp - 273.15
        self.temperature.setText(f"Temperature: {tempC:.2f}C")
        descr =data["weather"][0]["description"]
        self.desc.setText(f"{descr}")


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())