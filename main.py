# Ютуб-канал Crazy People хоче зробити окремий міні-конкурс для спонсорів каналу.
# Для них ютубери приготували складне питання з шістьма варіантами відповіді:

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
my_win = QWidget()
my_win.resize(500, 400)
my_win.setWindowTitle('міні-конкурс для спонсорів каналу')

def winn():
    # Якщо користувач вибирає правильний варіант відповіді, то з'являється вікно з повідомленням: «Ви виграли зустріч з творцями каналу!»
    message = QMessageBox()
    message.setText("Ви виграли зустріч з творцями каналу!")
    message.setIcon(QMessageBox.Question)
    message.exec()
def lose():
    # Якщо користувач вибирає будь-яку іншу відповідь, то з'являється вікно з повідомленням: «Пощастить іншим разом!»
    message = QMessageBox()
    message.setText("Пощастить іншим разом!")
    message.setIcon(QMessageBox.Critical)
    message.exec()

btn_ans1 = QRadioButton('PewDiePie')
btn_ans2 = QRadioButton('Рет і Лінк')
btn_ans3 = QRadioButton('SlivkiShow')
btn_ans4 = QRadioButton('TheBrianMaps')
btn_ans5 = QRadioButton('Mister Max')
btn_ans6 = QRadioButton('EeOneGuy')
queshion = QLabel('Як звали першого ютуб-блогера, який набрав 100 000 000 підписників?') # -> Як звали першого ютуб-блогера, який набрав 100 000 000 підписників?

line = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()

line.addWidget(queshion, alignment=Qt.AlignCenter)
line2.addWidget(btn_ans1, alignment=Qt.AlignCenter)
line2.addWidget(btn_ans2, alignment=Qt.AlignCenter)
line3.addWidget(btn_ans3, alignment=Qt.AlignLeft)
line3.addWidget(btn_ans4, alignment=Qt.AlignRight)
line4.addWidget(btn_ans5, alignment=Qt.AlignBottom|Qt.AlignHCenter)
line4.addWidget(btn_ans6, alignment=Qt.AlignBottom|Qt.AlignHCenter)

layout2 = QVBoxLayout()
layout2.addLayout(line)
layout2.addLayout(line2)
layout2.addLayout(line3)
layout2.addLayout(line4)
my_win.setLayout(layout2)

btn_ans1.clicked.connect(winn)
btn_ans2.clicked.connect(lose)
btn_ans3.clicked.connect(lose)
btn_ans4.clicked.connect(lose)
btn_ans5.clicked.connect(lose)
btn_ans6.clicked.connect(lose)

my_win.show()
app.exec()
