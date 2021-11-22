import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Circles(QMainWindow):
    def __init__(self):
        super(Circles, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.draw_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            n = randint(5, 15)
            for i in range(n):
                self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(100, self.size().width() - 100)
        y = randint(100, self.size().height() - 100)
        r = randint(1, 100)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec())
