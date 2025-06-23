# ui_expression_generator.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ვერტიკალური განლაგება
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)

        # გამოთქმის Label
        self.label_expression = QtWidgets.QLabel(self.centralwidget)
        self.label_expression.setText("აქ გამოჩნდება გამოთქმა")
        self.label_expression.setAlignment(QtCore.Qt.AlignCenter)
        self.label_expression.setMinimumHeight(60)
        self.label_expression.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_expression)

        # ღილაკი
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setText("ახალი გამოთქმა")
        self.verticalLayout.addWidget(self.btn_generate)

        # თემების ComboBox
        self.combo_topic = QtWidgets.QComboBox(self.centralwidget)
        self.combo_topic.addItems(["ყველაფერი", "გრძნობები", "ხასიათი"])
        self.verticalLayout.addWidget(self.combo_topic)

        # CheckBox – განმარტების ჩვენება
        self.checkbox_explanation = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_explanation.setText("გამომიტანე განმარტება")
        self.verticalLayout.addWidget(self.checkbox_explanation)

        # განმარტების Label
        self.label_explanation = QtWidgets.QLabel(self.centralwidget)
        self.label_explanation.setText("აქ გამოჩნდება განმარტება")
        self.label_explanation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_explanation.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_explanation)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("ქართული გამოთქმების გენერატორი")
