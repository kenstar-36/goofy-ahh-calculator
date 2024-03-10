# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(300, 450)
        widget.setMaximumSize(QSize(300, 450))
        font = QFont()
        font.setPointSize(35)
        widget.setFont(font)
        widget.setStyleSheet(u"background-color:black;")
        self.display_input = QLabel(widget)
        self.display_input.setObjectName(u"display_input")
        self.display_input.setGeometry(QRect(40, 100, 221, 51))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiCondensed"])
        font1.setPointSize(35)
        self.display_input.setFont(font1)
        self.display_input.setStyleSheet(u"color:white;")
        self.display_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.display_output = QLabel(widget)
        self.display_output.setObjectName(u"display_output")
        self.display_output.setGeometry(QRect(40, 30, 221, 51))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiCondensed"])
        font2.setPointSize(16)
        self.display_output.setFont(font2)
        self.display_output.setStyleSheet(u"color:white;")
        self.display_output.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 190, 271, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName(u"button_3")
        font3 = QFont()
        font3.setPointSize(17)
        self.button_3.setFont(font3)
        self.button_3.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_3, 2, 2, 1, 1)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font3)
        self.button_2.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_2, 2, 1, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setFont(font3)
        self.button_1.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_1, 2, 0, 1, 1)

        self.button_multiply = QPushButton(self.gridLayoutWidget)
        self.button_multiply.setObjectName(u"button_multiply")
        self.button_multiply.setFont(font3)
        self.button_multiply.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_multiply, 2, 3, 1, 1)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setFont(font3)
        self.button_minus.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_minus, 1, 3, 1, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setFont(font3)
        self.button_0.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_0, 3, 0, 1, 2)

        self.button_decimal = QPushButton(self.gridLayoutWidget)
        self.button_decimal.setObjectName(u"button_decimal")
        self.button_decimal.setFont(font3)
        self.button_decimal.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_decimal, 3, 2, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setFont(font3)
        self.button_8.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_8, 0, 1, 1, 1)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setFont(font3)
        self.button_7.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_7, 0, 0, 1, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setFont(font3)
        self.button_4.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setFont(font3)
        self.button_6.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setFont(font3)
        self.button_9.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_9, 0, 2, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setFont(font3)
        self.button_plus.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_plus, 0, 3, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setFont(font3)
        self.button_5.setStyleSheet(u"background-color:#2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)

        self.button_divide = QPushButton(self.gridLayoutWidget)
        self.button_divide.setObjectName(u"button_divide")
        self.button_divide.setFont(font3)
        self.button_divide.setStyleSheet(u"background-color:#EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_divide, 3, 3, 1, 1)

        self.button_clear = QPushButton(self.gridLayoutWidget)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setFont(font3)
        self.button_clear.setStyleSheet(u"background-color:white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_clear, 4, 0, 1, 2)

        self.button_equal = QPushButton(self.gridLayoutWidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setFont(font3)
        self.button_equal.setStyleSheet(u"background-color:white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.button_equal, 4, 2, 1, 2)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.display_input.setText(QCoreApplication.translate("widget", u"0", None))
        self.display_output.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_3.setText(QCoreApplication.translate("widget", u"3", None))
        self.button_2.setText(QCoreApplication.translate("widget", u"2", None))
        self.button_1.setText(QCoreApplication.translate("widget", u"1", None))
        self.button_multiply.setText(QCoreApplication.translate("widget", u"*", None))
        self.button_minus.setText(QCoreApplication.translate("widget", u"-", None))
        self.button_0.setText(QCoreApplication.translate("widget", u"0", None))
        self.button_decimal.setText(QCoreApplication.translate("widget", u".", None))
        self.button_8.setText(QCoreApplication.translate("widget", u"8", None))
        self.button_7.setText(QCoreApplication.translate("widget", u"7", None))
        self.button_4.setText(QCoreApplication.translate("widget", u"4", None))
        self.button_6.setText(QCoreApplication.translate("widget", u"6", None))
        self.button_9.setText(QCoreApplication.translate("widget", u"9", None))
        self.button_plus.setText(QCoreApplication.translate("widget", u"+", None))
        self.button_5.setText(QCoreApplication.translate("widget", u"5", None))
        self.button_divide.setText(QCoreApplication.translate("widget", u"/", None))
        self.button_clear.setText(QCoreApplication.translate("widget", u"c", None))
        self.button_equal.setText(QCoreApplication.translate("widget", u"=", None))
    # retranslateUi

