from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
my_win = QWidget()
my_win.resize(800, 400)
my_win.move(400, 400)
my_win.setWindowTitle("Лотерея")

btn = QPushButton("Випробувати удачу")
text = QLabel("Натисни, щоб взяти участь")
win = QLabel("?")
win2 = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(win, alignment=Qt.AlignCenter)
line.addWidget(win2, alignment=Qt.AlignCenter)
line.addWidget(btn, alignment=Qt.AlignCenter)
my_win.setLayout(line)

def show_win():
    number = randint(0, 9)
    number2 = randint(0, 9)
    win.setText(str(number))
    win2.setText(str(number2))
    if number == number2:
        text.setText(str("Ви виграли! Зіграйте знову"))
    else:
        text.setText(str("Ви програли! Зіграйте знову"))
btn.clicked.connect(show_win)

my_win.show()
app.exec_()