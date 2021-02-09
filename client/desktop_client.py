import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        #self.second_key = str(randint(10000, 99999))
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        button_generate = QPushButton('Generate Passwords')
        button_generate.clicked.connect(self.generate)
        layout.addWidget(button_generate, 0, 0, 1, 2)
        layout.setRowMinimumHeight(0, 75)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.generate)
        layout.addWidget(button_login, 1, 0, 1, 2)
        layout.setRowMinimumHeight(1, 75)

        self.setLayout(layout)

    def generate(self):
        msg = QMessageBox()

        try:
            sorge.generate_data(int(self.lineEdit_number.text()), self.lineEdit_key.text(), str(self.second_key))
            msg.setText('Success')
            msg.exec_()
        except:
            msg.setText('Incorrect Password')
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #rand = random(5)
    form = LoginForm()
    form.show()
    sys.exit(app.exec_())
