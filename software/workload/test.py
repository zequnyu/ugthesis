import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from time import strftime

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
        self.lcd = QLCDNumber(self)
        self.lcd.display(strftime("%S"))
        self.setCentralWidget(self.lcd)
        self.setGeometry(300,300,250,100)

    def Time(self):
        if int(strftime("%S")) % 10 == 0:
            self.timer.setInterval(5000)
        else:
            self.timer.setInterval(1000)
        self.lcd.display(strftime("%S"))

def main():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
