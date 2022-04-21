from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GUI import Ui_MainWindow
import sys
from math import pi, sin, cos
import scipy.stats as stats


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("My app")

        ##########################################
        self.ui.pushButton.clicked.connect(self.get_max_height)
        self.ui.pushButton.clicked.connect(self.get_height_of_arrival)
        self.ui.pushButton_2.clicked.connect(self.get_propability)
        self.ui.clear_1.clicked.connect(self.Clear_1)
        self.ui.clear_2.clicked.connect(self.Clear_2)

        #########################################

    def get_max_height(self):
        try:
            self.velocity = float(self.ui.lineEdit_2.text())
            self.theta = float(self.ui.lineEdit_3.text())
            self.theta1 = (self.theta * pi) / 180
            self.xvel = self.velocity * cos(self.theta1)
            self.yvel = self.velocity * sin(self.theta1)
            self.max_height = round(pow(self.yvel, 2) / (2 * 9.81), 2)
            self.max_height = str(self.max_height)
            self.ui.label_7.setText(self.max_height)
        except Exception as e:
            print("ERROR: you should add value")

    def get_height_of_arrival(self):
        try:
            self.distance_to_goal = float(self.ui.lineEdit.text())
            self.time_of_flight = self.distance_to_goal / self.xvel
            self.result = (self.yvel * self.time_of_flight) + ((-9.8 * pow(self.time_of_flight, 2)) / 2.0)
            self.arrival_height = str(round(self.result, 3))
            self.ui.label_8.setText(self.arrival_height)
        except Exception as e:
            self.error_message("ERROR", str("you should add values"))

    def get_propability(self):
        try:
            self.ball_hit_speed = int(self.ui.lineEdit_7.text())
            result = stats.norm.cdf(self.ball_hit_speed, 160, 20)
            result = round(result, 3)
            self.cumulative_probability = str(result)
            self.ui.label_18.setText(self.cumulative_probability)
        except Exception as e:
            self.error_message("ERROR", str("you should add value"))

    def Clear_1(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.label_8.clear()
        self.ui.label_7.clear()

    def Clear_2(self):
        self.ui.lineEdit_7.clear()
        self.ui.label_18.clear()

    def error_message(self, title, msg):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(msg)
        msgbox.setIcon(msgbox.Critical)
        msgbox.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
