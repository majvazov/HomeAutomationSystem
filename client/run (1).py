import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from random import randint
import sorge

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.second_key = str(randint(10000, 99999))
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_key = QLabel('<font size="4"> Encryption KEY </font>')
        self.lineEdit_key = QLineEdit()
        self.lineEdit_key.setPlaceholderText('Please enter your encryption key')
        layout.addWidget(label_key, 0, 0)
        layout.addWidget(self.lineEdit_key, 0, 1)

        label_number = QLabel('<font size="4"> Number of users </font>')
        self.lineEdit_number = QLineEdit()
        self.lineEdit_number.setPlaceholderText('Please enter number of users')
        layout.addWidget(label_number, 1, 0)
        layout.addWidget(self.lineEdit_number, 1, 1)

        button_generate = QPushButton('Generate Passwords')
        button_generate.clicked.connect(self.generate)
        layout.addWidget(button_generate, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 3, 0)
        layout.addWidget(self.lineEdit_username, 3, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 4, 0)
        layout.addWidget(self.lineEdit_password, 4, 1)

        label_kd = QLabel('<font size="4"> KD </font>')
        self.lineEdit_kd = QLineEdit()
        self.lineEdit_kd.setPlaceholderText('Please enter your Kd')
        layout.addWidget(label_kd, 5, 0)
        layout.addWidget(self.lineEdit_kd, 5, 1)



        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 6, 0, 1, 2)
        layout.setRowMinimumHeight(6, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if sorge.check_if_password_matches(int(self.lineEdit_username.text()), self.lineEdit_password.text(), self.lineEdit_key.text(), str(self.second_key)):
            if sorge.check_if_kd_matches(int(self.lineEdit_username.text()), self.lineEdit_kd.text(), self.lineEdit_key.text(), str(self.second_key)):
                msg.setText('Success')
                msg.exec_()
            else:
                msg.setText('Incorrect Kd')
                msg.exec_()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

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
