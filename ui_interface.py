# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceFJcIZy.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget

from PySide6.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 785)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Header = QFrame(self.centralwidget)
        self.frame_Header.setObjectName(u"frame_Header")
        self.frame_Header.setMaximumSize(QSize(16777215, 60))
        self.frame_Header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_Header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_Left_Signal = QLabel(self.frame_Header)
        self.lb_Left_Signal.setObjectName(u"lb_Left_Signal")
        self.lb_Left_Signal.setMaximumSize(QSize(60, 60))
        self.lb_Left_Signal.setPixmap(QPixmap(u"left_arrow.png"))
        self.lb_Left_Signal.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lb_Left_Signal)

        self.lb_App_Title = QLabel(self.frame_Header)
        self.lb_App_Title.setObjectName(u"lb_App_Title")
        font = QFont()
        font.setPointSize(22)
        self.lb_App_Title.setFont(font)
        self.lb_App_Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_App_Title)

        self.lb_Right_Signal = QLabel(self.frame_Header)
        self.lb_Right_Signal.setObjectName(u"lb_Right_Signal")
        self.lb_Right_Signal.setMaximumSize(QSize(60, 60))
        self.lb_Right_Signal.setPixmap(QPixmap(u"right_arrow.png"))
        self.lb_Right_Signal.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lb_Right_Signal)


        self.verticalLayout.addWidget(self.frame_Header)

        self.frame_Body = QFrame(self.centralwidget)
        self.frame_Body.setObjectName(u"frame_Body")
        sizePolicy.setHeightForWidth(self.frame_Body.sizePolicy().hasHeightForWidth())
        self.frame_Body.setSizePolicy(sizePolicy)
        self.frame_Body.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_Body)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Left_Analog = QFrame(self.frame_Body)
        self.frame_Left_Analog.setObjectName(u"frame_Left_Analog")
        self.frame_Left_Analog.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Left_Analog.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Left_Analog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Analog_Gauge_Speed = AnalogGaugeWidget(self.frame_Left_Analog)
        self.Analog_Gauge_Speed.setObjectName(u"Analog_Gauge_Speed")
        sizePolicy.setHeightForWidth(self.Analog_Gauge_Speed.sizePolicy().hasHeightForWidth())
        self.Analog_Gauge_Speed.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.Analog_Gauge_Speed)


        self.horizontalLayout_3.addWidget(self.frame_Left_Analog)

        self.frame_Center = QFrame(self.frame_Body)
        self.frame_Center.setObjectName(u"frame_Center")
        self.frame_Center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Center.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_Center)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_Charging = QRadioButton(self.frame_Center)
        self.btn_Charging.setObjectName(u"btn_Charging")
        font1 = QFont()
        font1.setPointSize(16)
        self.btn_Charging.setFont(font1)
        self.btn_Charging.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_Charging, 0, 0, 1, 1)

        self.btn_Brake = QRadioButton(self.frame_Center)
        self.btn_Brake.setObjectName(u"btn_Brake")
        self.btn_Brake.setFont(font1)
        self.btn_Brake.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_Brake.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_Brake, 0, 1, 1, 1)

        self.btn_Front = QRadioButton(self.frame_Center)
        self.btn_Front.setObjectName(u"btn_Front")
        self.btn_Front.setFont(font1)
        self.btn_Front.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_Front, 1, 0, 1, 1)

        self.btn_Rear = QRadioButton(self.frame_Center)
        self.btn_Rear.setObjectName(u"btn_Rear")
        self.btn_Rear.setFont(font1)
        self.btn_Rear.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btn_Rear.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btn_Rear, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_Center)

        self.frame_Right_Analog = QFrame(self.frame_Body)
        self.frame_Right_Analog.setObjectName(u"frame_Right_Analog")
        self.frame_Right_Analog.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Right_Analog.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Right_Analog)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_Cam = QLabel(self.frame_Right_Analog)
        self.lb_Cam.setObjectName(u"lb_Cam")

        self.verticalLayout_4.addWidget(self.lb_Cam)


        self.horizontalLayout_3.addWidget(self.frame_Right_Analog)


        self.verticalLayout.addWidget(self.frame_Body)

        self.frame_Footer = QFrame(self.centralwidget)
        self.frame_Footer.setObjectName(u"frame_Footer")
        self.frame_Footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Footer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_Footer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WebEngineContainer = QWidget(self.frame_Footer)
        self.WebEngineContainer.setObjectName(u"WebEngineContainer")
        self.verticalLayout_5 = QVBoxLayout(self.WebEngineContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.WebView = QWebEngineView(self.WebEngineContainer)
        self.WebView.setObjectName(u"WebView")

        self.verticalLayout_5.addWidget(self.WebView)


        self.verticalLayout_2.addWidget(self.WebEngineContainer)


        self.verticalLayout.addWidget(self.frame_Footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UIT CAR DASHBOARD", None))
        self.lb_Left_Signal.setText("")
        self.lb_App_Title.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#0055ff;\">UIT CAR DASHBOARD</span></p></body></html>", None))
        self.lb_Right_Signal.setText("")
        self.btn_Charging.setText(QCoreApplication.translate("MainWindow", u"Changing", None))
        self.btn_Brake.setText(QCoreApplication.translate("MainWindow", u"Brake", None))
        self.btn_Front.setText(QCoreApplication.translate("MainWindow", u"Front", None))
        self.btn_Rear.setText(QCoreApplication.translate("MainWindow", u"Rear", None))
        self.lb_Cam.setText("")
    # retranslateUi

