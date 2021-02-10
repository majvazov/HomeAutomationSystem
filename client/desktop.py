import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt, QRect
from devices import Device, DeviceManager

class MySwitch(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        print('init')
        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event):
        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.red

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(center)
        painter.setBrush(QtGui.QColor(0,0,0))

        pen = QtGui.QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2*width, 2*radius), radius, radius)
        painter.setBrush(QtGui.QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2*radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignCenter, label)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.espState = False
        #self.second_key = str(randint(10000, 99999))
        self.setWindowTitle('IoT Device Manager')
        self.resize(500, 120)
        self.devices = DeviceManager()
        layout = QGridLayout()

        ch_bx1 = MySwitch()
        ch_bx1.setChecked(True)
        ch_bx1.clicked.connect(self.changeStateOne)
        layout.addWidget(ch_bx1, 0, 0, 1, 2)

        #self.device = Device('ESP32', 'ESP1', '192.168.12.11', "OFF")

        ch_bx3 = MySwitch()
        ch_bx3.setChecked(True)
        ch_bx3.clicked.connect(self.changeStateTwo)
        layout.addWidget(ch_bx3, 1, 0, 1, 2)

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

    def changeStateOne(self):
        self.devices.devices[0].changeState()
        return 0

    def changeStateTwo(self):
        self.devices.devices[1].changeState()
        return 0

    def create_devices(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    #rand = random(5)
    form = Window()
    form.show()
    sys.exit(app.exec_())
