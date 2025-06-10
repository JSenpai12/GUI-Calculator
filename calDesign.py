# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(320, 346)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        Calculator.setWindowIcon(icon)
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 302, 61))
        self.frame.setMaximumSize(QSize(16777215, 165))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 301, 61))
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 30px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(16)
        self.label.setIndent(0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 76, 301, 261))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(16777215, 168))
        self.pushButton_9.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_9, 2, 5, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(16777215, 168))
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet(u"background-color: #f5923e;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 30px;")

        self.gridLayout.addWidget(self.pushButton_16, 3, 6, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(16777215, 168))
        self.pushButton_7.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(16777215, 168))
        self.pushButton_11.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_11, 0, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(16777215, 168))
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(u"background-color: #f5923e;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 30px;")

        self.gridLayout.addWidget(self.pushButton_14, 1, 6, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(16777215, 168))
        self.pushButton_8.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_8, 2, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 168))
        self.pushButton.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 168))
        self.pushButton_2.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_2, 1, 5, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(16777215, 168))
        font = QFont()
        font.setBold(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet(u"background-color: #f5923e;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 30px;")

        self.gridLayout.addWidget(self.pushButton_15, 2, 6, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 168))
        self.pushButton_6.setStyleSheet(u"background-color: #f5923e;\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.pushButton_6, 3, 5, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(16777215, 168))
        self.pushButton_12.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_12, 0, 5, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 168))
        self.pushButton_5.setStyleSheet(u"background-color: #8b8c8c;\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: bold;")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(16777215, 168))
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet(u"background-color: #f5923e;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 30px;")

        self.gridLayout.addWidget(self.pushButton_13, 0, 6, 1, 1)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(16777215, 168))
        self.pushButton_10.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_10, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 168))
        self.pushButton_4.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_4, 3, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 168))
        self.pushButton_3.setStyleSheet(u"background-color: #4c4c4c;\n"
"color: white;\n"
"font-weight: normal;\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)

        Calculator.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.label.setText(QCoreApplication.translate("Calculator", u"", None))
        self.pushButton_9.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pushButton_16.setText(QCoreApplication.translate("Calculator", u"+", None)) 
        self.pushButton_7.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pushButton_11.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pushButton_14.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pushButton.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pushButton_15.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.pushButton_12.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pushButton_5.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.pushButton_13.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.pushButton_10.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calculator", u"4", None))
    # retranslateUi

