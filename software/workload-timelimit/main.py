import sys
from welcome import Welcome
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self, h, w):
        super(MainWindow, self).__init__()
        self.widgetList = QStackedWidget()
        self.widgetList.setFixedSize(w, h)
        self.setCentralWidget(self.widgetList)
        self.widgetList.addWidget(Welcome(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QLabel{color: #ffffff;}')
    h = app.desktop().screenGeometry().height()
    w = app.desktop().screenGeometry().width()
    window = MainWindow(h, w)
    window.show()
    sys.exit(app.exec_())
