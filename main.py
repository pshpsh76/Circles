import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.draw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.draw_btn.setGeometry(QtCore.QRect(140, 30, 271, 41))
        self.draw_btn.setObjectName("draw_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.draw_btn.setText(_translate("MainWindow", "Нарисовать кружки"))


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Circles, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.draw_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            n = randint(5, 30)
            for i in range(n):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                self.draw_circle(qp, QColor(r, g, b))
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_circle(self, qp, color):
        qp.setBrush(color)
        x = randint(100, self.size().width() - 100)
        y = randint(100, self.size().height() - 100)
        r = randint(1, 100)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec())
