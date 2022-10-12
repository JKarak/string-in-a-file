import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cnt = 0

    def initUI(self):
        self.setGeometry(300, 500, 500, 500)
        self.setWindowTitle("Случайная строка")
        self.line1 = QLineEdit("", self)
        self.line1.move(140, 100)
        self.line1.resize(200, 50)

        self.btn = QPushButton("Получить", self)
        self.btn.move(0, 100)
        self.btn.resize(140, 50)
        self.btn.clicked.connect(self.click)

    def click(self):
        with open("something.txt") as f:
            lines = f.readlines()

        random_line = random.choice(lines).strip()
        self.line1.setText(random_line)

    def hello(self):
        # метод setText() используется для задания надписи на кпопке
        self.line1.setText('Привет')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
