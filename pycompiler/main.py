from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(0, 0, 55, 55))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(222, 222, 222);\n"
                                     "    color: rgb(0, 204, 102);\n"
                                     "}\n"
                                     "QPushButton: hover {\n"
                                     "    background-color: rgb(100, 100, 100);\n"
                                     "}")
        self.runButton.setObjectName("runButton")
        self.Code = QtWidgets.QTextEdit(self.centralwidget)
        self.Code.setGeometry(QtCore.QRect(0, 56, 1200, 745))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Code.setFont(font)
        self.Code.setStyleSheet("background-color: rgb(130, 130, 130); color: rgb(102, 0, 102);")
        self.Code.setObjectName("Code")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(56, 0, 1145, 55))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def add_functions(self):
        self.runButton.clicked.connect(lambda:  self.run_code())

    def run_code(self):
        with open('run.py', 'w') as file:
            file.write(self.Code.toPlainText())
            file.close()
        command = 'python run.py'
        os.system(command)
        time.sleep(30)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runButton.setText(_translate("MainWindow", "▶"))
        self.label.setText(_translate("MainWindow", "Write and run you code! :)"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
