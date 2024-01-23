from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QApplication,
QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.setStyleSheet('background-color: #DCDCDC; color: #191970; font-size: 25px')


'''Інтерфейс калькулятора'''
line_edit = QLineEdit()
number_0 = QPushButton('0')
number_1 = QPushButton('1')
number_2 = QPushButton('2')
number_3 = QPushButton('3')
number_4 = QPushButton('4')
number_5 = QPushButton('5')
number_6 = QPushButton('6')
number_7 = QPushButton('7')
number_8 = QPushButton('8')
number_9 = QPushButton('9')

act_plus = QPushButton('+')
act_minus = QPushButton('-')
act_multiply = QPushButton('*')
act_divide = QPushButton('/')

button_point = QPushButton('.')
button_delete = QPushButton('CE')
button_equals = QPushButton('=')


act_plus.setStyleSheet('background-color: #DAA520')
act_minus.setStyleSheet('background-color: #DAA520')
act_multiply.setStyleSheet('background-color: #DAA520')
act_divide.setStyleSheet('background-color: #DAA520')
act_divide.setFixedWidth(75)

h1 = QHBoxLayout()
h1.addWidget(number_7)
h1.addWidget(number_8)
h1.addWidget(number_9)
h1.addWidget(act_plus)

h2 = QHBoxLayout()
h2.addWidget(number_4)
h2.addWidget(number_5)
h2.addWidget(number_6)
h2.addWidget(act_minus)

h3 = QHBoxLayout()
h3.addWidget(number_1)
h3.addWidget(number_2)
h3.addWidget(number_3)
h3.addWidget(act_multiply)

h4 = QHBoxLayout()
h4.addWidget(button_point)
h4.addWidget(number_0)
h4.addWidget(act_divide)

h5 = QHBoxLayout()
h5.addWidget(button_delete)
h5.addWidget(button_equals)

main_layout = QVBoxLayout()
main_layout.addWidget(line_edit)
main_layout.addLayout(h1)
main_layout.addLayout(h2)
main_layout.addLayout(h3)
main_layout.addLayout(h4)
main_layout.addLayout(h5)

window.setLayout(main_layout)


'''Вікно'''
window.show()
app.exec()
