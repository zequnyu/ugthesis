import sys
from finished import Finished
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, QElapsedTimer, QTimer
from time import strftime


class Question(QWidget):

    def __init__(self, mainWindow, questionNum, result, timer, selectedInx):
        super().__init__()
        self.questionNum = questionNum
        self.mainWindow = mainWindow
        self.result = result
        self.timer = timer
        self.selectedInx = selectedInx
        self.currentSelectedIndex = self.selectedInx[self.questionNum-1]
        self.setMaximumSize(1920, 1080)
        self.initPage()

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
        t = QLabel('Question ' + str(self.questionNum), self)
        t.setFont(QFont('SansSerif', 48))
        t.setAlignment(Qt.AlignCenter)

        q = QLabel(self)
        pixmap = QPixmap('questions/q/img_q' + str(self.currentSelectedIndex) + '.png')
        q.setPixmap(pixmap)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(t, 0, 2, Qt.AlignCenter)
        self.mainLayout.addWidget(q, 0, 3, Qt.AlignCenter)

        fi = "{0:0=2d}".format(self.currentSelectedIndex)
        self.bs = []
        for j in range(0, 8):
            cur_base_col = j%4
            cur_base_row = j//4
            a = QLabel(self)
            pixmap = QPixmap('questions/a/img_a'+fi+str(j//4+1)+str(j%4+1)+'.png')
            a.setPixmap(pixmap)
            b = QRadioButton(str(j+1), self)
            b.setStyleSheet("color: #ffffff");
            if j==0:
                b.setChecked(True)

            self.bs.append(b)
            self.mainLayout.addWidget(a, 1+cur_base_row*2, cur_base_col+1, Qt.AlignCenter)
            self.mainLayout.addWidget(b, 1+cur_base_row*2+1, cur_base_col+1, Qt.AlignCenter)

        if self.questionNum % 5 == 0:
            btn = QPushButton("Rate")
            btn.clicked.connect(self.toRate)
        else:
            btn = QPushButton("Next")
            btn.clicked.connect(self.nextQuestion)
        btn.setMaximumSize(QSize(256, 128))
        btn.setMinimumSize(QSize(128, 64))

        self.mainLayout.addWidget(btn, 5, 3, Qt.AlignCenter)
        self.setLayout(self.mainLayout)

    def toRate(self):
        self.updateResult()
        self.updateTime()
        timer = QElapsedTimer()
        timer.start()
        rateWidget = Rate(self.mainWindow, self.questionNum, self.result, self.selectedInx, timer)
        self.mainWindow.widgetList.addWidget(rateWidget)
        self.mainWindow.widgetList.setCurrentWidget(rateWidget)

    def nextQuestion(self):
        self.updateResult()
        questionWidget = Question(self.mainWindow, self.questionNum+1, self.result, self.timer, self.selectedInx)
        self.mainWindow.widgetList.addWidget(questionWidget)
        self.mainWindow.widgetList.setCurrentWidget(questionWidget)

    def updateResult(self):
        for i in range(0, 8):
            if self.bs[i].isChecked():
                self.result.updateAnswer(self.questionNum-1, i+1)

    def updateTime(self):
        self.result.updateTime(self.questionNum//5-1, self.timer.elapsed())




class Rate(QWidget):

    def __init__(self, mainWindow, questionNum, result, selectedInx, timer):
        super().__init__()
        self.questionNum = questionNum
        self.mainWindow = mainWindow
        self.result = result
        self.selectedInx = selectedInx
        self.timer = timer
        self.setMaximumSize(1920, 1080)
        self.initPage()


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
        t = QLabel('Please rate your workload (1-low, 5-high) for Q' + str(self.questionNum-4) + '-' + str(self.questionNum), self)
        t.setFont(QFont('SansSerif', 48))
        t.setAlignment(Qt.AlignCenter)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(t, 0, 0, Qt.AlignCenter)

        self.bs = []
        for j in range(0, 5):
            b = QRadioButton(str(j+1), self)
            b.setStyleSheet("color: #ffffff");
            if j==0:
                b.setChecked(True)
            self.bs.append(b)
            self.mainLayout.addWidget(b, 1+j, 0, Qt.AlignCenter)


        if self.questionNum == 20:
            btn = QPushButton("Finish")
            btn.setMaximumSize(QSize(256, 128))
            btn.setMinimumSize(QSize(128, 64))
            btn.clicked.connect(self.submitResult)
        else:
            btn = QPushButton("Next Q")
            btn.clicked.connect(self.relaxTime)
            btn.setMaximumSize(QSize(256, 128))
            btn.setMinimumSize(QSize(128, 64))

        self.mainLayout.addWidget(btn, 6, 0, Qt.AlignCenter)
        self.setLayout(self.mainLayout)

    def relaxTime(self):
        self.updateRate()
        self.updateTime()
        tb = Timebreak(self.mainWindow, self.questionNum, self.result, self.selectedInx)
        self.mainWindow.widgetList.addWidget(tb)
        self.mainWindow.widgetList.setCurrentWidget(tb)

    def updateRate(self):
        for i in range(0, 5):
            if self.bs[i].isChecked():
                self.result.updateRate(self.questionNum//5-1, i+1)

    def updateTime(self):
        self.result.updateRateTime(self.questionNum//5-1, self.timer.elapsed())

    def submitResult(self):
        self.updateRate()
        self.updateTime()
        self.result.printResult()
        finished = Finished(self.mainWindow)
        self.mainWindow.widgetList.addWidget(finished)
        self.mainWindow.widgetList.setCurrentWidget(finished)


class Timebreak(QWidget):
    def __init__(self, mainWindow, questionNum, result, selectedInx):
        super().__init__()
        self.initPage()
        self.mainWindow = mainWindow
        self.questionNum = questionNum
        self.result = result
        self.selectedInx = selectedInx

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
        self.count = 15
        self.label1 = QLabel('Relax Time\n\n\n\n', self)
        self.label1.setFont(QFont('SansSerif', 48))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2 = QLabel('Please do not think of anything else.\nTake a deep breath.\nYou could close your eyes.', self)
        self.label2.setFont(QFont('SansSerif', 36))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3 = QLabel('Please relax for '+str(self.count)+' seconds!', self)
        self.label3.setFont(QFont('SansSerif', 36))
        self.label3.setAlignment(Qt.AlignCenter)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateLabel)
        self.timer.start(1000)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addWidget(self.label2)
        self.mainLayout.addWidget(self.label3)
        self.setLayout(self.mainLayout)

    def updateLabel(self):
        self.count = self.count - 1
        self.label3.setText('Please relax for '+str(self.count)+' seconds!')
        if self.count <= 0:
            self.timer.stop()
            self.nextQuestion()

    def nextQuestion(self):
        timer = QElapsedTimer()
        timer.start()
        questionWidget = Question(self.mainWindow, self.questionNum+1, self.result, timer, self.selectedInx)
        self.mainWindow.widgetList.addWidget(questionWidget)
        self.mainWindow.widgetList.setCurrentWidget(questionWidget)
