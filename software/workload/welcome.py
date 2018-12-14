import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, QElapsedTimer, QTimer
from question import Question
from result import Result


class Welcome(QWidget):

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
        label1 = QLabel('\n\n\nWorkload Test\n\n\n', self)
        label1.setFont(QFont('SansSerif', 48))
        label1.setAlignment(Qt.AlignCenter)
        text = "You are invited to answer a questionnaire of 20 questions\n" \
        " and rate your workload in 5-point scale. Please focus yourself\n" \
        " on the questions as much as you can and do not think of anything else.\n\n\n"
        label2 = QLabel(text, self)
        label2.setFont(QFont('SansSerif', 36))
        label2.setAlignment(Qt.AlignCenter)
        label3 = QLabel('Click button to see example question. The test begins in 15 seconds after that.', self)
        label3.setFont(QFont('SansSerif', 24))
        label3.setAlignment(Qt.AlignCenter)

        btn = QPushButton("See Example Question")
        btn.clicked.connect(self.exampleQuestion)
        btn.setMaximumSize(QSize(256, 128))
        btn.setMinimumSize(QSize(128, 64))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(label1, 1, Qt.AlignCenter)
        mainLayout.addWidget(label2, 3, Qt.AlignCenter)
        mainLayout.addWidget(label3, 5, Qt.AlignCenter)
        mainLayout.addWidget(btn, 6, Qt.AlignCenter)
        self.setLayout(mainLayout)

    def exampleQuestion(self):
        e = Example(self.mainWindow)
        self.mainWindow.widgetList.addWidget(e)
        self.mainWindow.widgetList.setCurrentWidget(e)


class Example(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.initPage()
        self.mainWindow = mainWindow
        self.result = Result()
        #EHEH
        self.selectedInx = [1, 2, 7, 8, 9, 19, 20, 34, 36, 37, 4, 6, 11, 12, 15, 24, 25, 27, 30, 32]
        #HEHE
        #[19, 20, 34, 36, 37, 1, 2, 7, 8, 9, 24, 25, 27, 30, 32, 4, 6, 11, 12, 15]

    def initPage(self):
        self.setMainLayout()
        self.setWindowTitle('Example Question')
        self.setBackgroundColor()

    def setBackgroundColor(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#333333'))
        self.setPalette(p)

    def setMainLayout(self):
        label1 = QLabel('\n\nExample Question\n', self)
        label1.setFont(QFont('SansSerif', 48))
        label1.setAlignment(Qt.AlignCenter)
        q = QLabel(self)
        pixmap = QPixmap('e.png')
        q.setPixmap(pixmap)
        q.setMaximumSize(QSize(1200, 800))
        q.setMinimumSize(QSize(900, 600))

        self.count = 15
        self.label3 = QLabel('Test starts after '+str(self.count)+' seconds!', self)
        self.label3.setFont(QFont('SansSerif', 36))
        self.label3.setAlignment(Qt.AlignCenter)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabel)
        self.timer.start(1000)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(label1, 0, Qt.AlignCenter)
        mainLayout.addWidget(q, 1, Qt.AlignCenter)
        mainLayout.addWidget(self.label3, 2, Qt.AlignCenter)
        self.setLayout(mainLayout)

    def updateLabel(self):
        self.count = self.count - 1
        self.label3.setText('Test starts after '+str(self.count)+' seconds!')
        if self.count <= 0:
            self.timer.stop()
            self.startTest()


    def startTest(self):
        questionNum = 0
        timer = QElapsedTimer()
        timer.start()

        questionWidget = Question(self.mainWindow, questionNum+1, self.result, timer, self.selectedInx)
        self.mainWindow.widgetList.addWidget(questionWidget)
        self.mainWindow.widgetList.setCurrentWidget(questionWidget)
