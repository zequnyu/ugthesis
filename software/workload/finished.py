from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt, QSize, QElapsedTimer


class Finished(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.initPage()
        self.mainWindow = mainWindow

    def initPage(self):
        self.setMainLayout()
        self.setWindowTitle('Workload Test')
        self.setBackgroundColor()

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#333333'))
        self.setPalette(p)

    def setMainLayout(self):
        label1 = QLabel('Thank you!', self)
        label1.setFont(QFont('SansSerif', 48))
        label1.setAlignment(Qt.AlignCenter)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(label1)

        self.setLayout(mainLayout)
